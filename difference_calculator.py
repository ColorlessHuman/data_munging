class MinDifferenceCalculator:
    """MinDifferenceCalculator module

    This module accepts a data file path calculates the minimum difference
    between two columns specified

    Attributes:
        filepath (str): Path to the data file
        col1 (int): Column 1 of the difference pair
        col2 (int): Column 2 of the difference pair
        result_col (int): The column which is to be displayed once minimum
            difference is calculated
    """


    def __init__(self, filepath, col1, col2, result_col):
        """Constructor function for MinDifferenceCalculator class.

        Args:
            self (MinDifferenceCalculator): self object of class
                MinDifferenceCalculator
            filepath (str): Path to data file
            col1 (int): Column 1 of the difference pair
            col2 (int): Column 2 of the difference pair
            result_col (int): The column which is to be displayed once minimum
                difference is calculated

        Returns:
            None
        """
        self.filepath = filepath
        self.col1 = col1
        self.col2 = col2
        self.result_col = result_col
        # print(self.filepath, self.col1, self.col2, self.result_col)


    def get_min_difference(self):
        """Function to calculate min difference and return desired column.

        Args:
            self (MinDifferenceCalculator): self object of class
                MinDifferenceCalculator

        Returns:
            int: result_value
        """
        with open(self.filepath, 'r') as file_handler:
            line = file_handler.readline()
            headers = list(line.split())
            line = file_handler.readline()
            items = list(line.split())
            """If line is empty parse next line"""
            if items == []:
                line = file_handler.readline()
                items = list(line.split())
            min_difference = abs(float(items[self.col1]) - float(items[self.col2]))
            result_value = items[self.result_col]

            for line in file_handler.readlines():
                items = list(line.split())
                """If line is empty parse next line"""
                if items == []:
                    continue

                for item in items:
                    items[items.index(item)] = item.strip('*')
                try:
                    if min_difference >= abs((float(items[self.col1]) - float(items[self.col2]))):
                        min_difference = abs(float(items[self.col1]) - float(items[self.col2]))
                        result_value = items[self.result_col]
                except IndexError:
                    pass

        return result_value
