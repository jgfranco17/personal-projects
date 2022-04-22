"""
Created on 12 Sept 2021 
@author: Chino Franco

COVID-19 data tracking for different countries using API requests from https://api.covid19api.com/ routes
"""

import matplotlib.pyplot as plt
import requests
import json
import numpy as np
import datetime as dt
import traceback as tb

class CovidData(object):
    def __init__(self, country:str):
        self.country = country.title()
        self.data = {
            "Dates": list(),
            "Active": list(),
            "Confirmed": list(),
            "Recovered": list()
        }
        self.point_count = 0
        self.categories = ", ".join(self.data.keys())
        
    def __len__(self):
        return self.point_count
    
    def __repr__(self):
        return f'CovidData({self.country}, {self.point_count} data points)'
    
    def __str__(self):
        return f'{self.country} cases'
    
    def __eq__(self, other):
        return self.country == other.country
    
    def processing(func):
        """
        Takes the stored country name and gathers data from the API, 
        stores it in the object's data property.
        
        Wrapper function, used to run data retrieval and processing prior
        to the execution of another data-dependent functions.
        """
        def load_data(self, *args, **kwargs):
            url = f'https://api.covid19api.com/total/country/{self.country.lower()}'
            
            try:
                # Get JSON data via API call
                info = json.loads(requests.get(url).text)
                self.point_count = int(len(info))
                for point in range(self.point_count):  # Gathers day for each day
                    datapoint = info[point]
                    point_date = dt.datetime.strptime(datapoint["Date"], '%Y-%m-%dT%H:%M:%SZ')
                    
                    # Store data to object collection
                    self.data["Dates"].append(point_date.strftime("%d %b %Y"))
                    self.data["Active"].append(datapoint["Active"])
                    self.data["Confirmed"].append(datapoint["Confirmed"])
                    self.data["Recovered"].append(datapoint["Recovered"])
                    
                print(f'{self.point_count} data points gathered for {self.country}.')
                
                return func(self, *args, **kwargs)
                
            except Exception as e:
                print(f'ERROR - Data failed to compile.\nReason: {e}')
                tb.print_exc()   

        return load_data
    
    @processing
    def get_present_cases(self) -> dict:
        """
        Gets the data of cases as of today.        

        Returns:
            dict: collection of today's data
        """
        return {key: self.data[key][-1] for key in self.data.keys()}
    
    @processing
    def case_updates(self, category:str, span:int, **kwargs):
        """
        Gets the data of cases over a given span of days. Compares the data analytically.

        Args:
            category (str): Data set to retrieve
            span (int): Number of days back to be examined
            
        Keyword Args:
            start (int): Date to start the analysis
            end (int): Date to end the analysis
            analysis (str): Type of analysis to be performed
        """
        try:
            data_set = [self.data[category][-day] for day in range(1, span+1)]
            data_set.reverse()
            print(f"{category}: {self.get_present_cases()}")
            print(data_set, kwargs)
            print(f"Standard deviation over {span} days: {np.std(data_set):.2f}")
            
        except Exception as e:
            print(f'ERROR - Data failed to compare.\nReason: {e}')
    
    @processing
    def data_plot(self, category=None):
        """[summary]
        Generates plot of country data from Day 1 to present.
        
        Args:
            dataset (str, optional): Data set to retrieve. Defaults to None.
        """
        if category is not None and category in self.data.keys():
            try:
                # Convert data to NumPy array
                plot_x = np.array(self.data["Dates"])
                plot_y = np.array(self.data[category])
                
                # Plot data
                plt.plot(range(1, len(plot_x)+1), plot_y, 'r-', label=category)
                plt.grid(True)
                plt.xlim(0, self.point_count)
                plt.ylim(0, np.amax(self.data[category]))
                plt.xlabel('Days since 1st case')
                plt.ylabel(category)
                plt.title(f'COVID-19 Data: {self.country}')
                plt.legend()
                plt.show()
            
            except Exception as e:
                print(f'ERROR - Data failed to plot.\nReason: {e}')
                
        else:
            print('WARNING: No data to plot! Please include a valid parameter indicating which data to print.')
            print(f'Valid entries: {", ".join(self.data.keys())}')
        
    
if __name__ == "__main__":
    location = 'Japan'
    category = 'Active'
    
    tracker = CovidData(location)
    tracker.case_updates('Confirmed', 10, analysis='linear')
    # tracker.data_plot(category)
