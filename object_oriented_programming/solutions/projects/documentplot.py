# Write a Python program that inputs a document and then outputs a bar-chart plot
# of the frequencies of each alphabet character that appears in that document.

import re
import altair
import altair as alt
import numpy as np
import pandas as pd
import os
from altair import Chart


class ReadDocument:
    def __init__(self, file_path: str | os.PathLike):
        self._file_path = file_path

    def open_file(self) -> str:
        document = open(self._file_path, 'r').read()
        return document

    def parse_file(self) -> tuple:
        regex = re.compile('[^a-zA-Z]')
        document_file = regex.sub('', self.open_file())
        document_file_count = document_file.count
        print(document_file_count)
        input_document = list(document_file.replace(' ', '')) # removing blank space
        alphabets, frequency = np.unique(input_document, return_counts=True)
        return alphabets, frequency

    def _data(self) -> pd.DataFrame:
        alphabets, frequency = self.parse_file()
        data_file = pd.DataFrame({'Alphabets': alphabets, 'Frequency': frequency})
        return data_file

    def bar_chart_plot(self) -> Chart:
        return altair.Chart(self._data()).mark_bar().encode(
            x='Alphabets:N',
            y=alt.Y('Frequency:Q', axis=alt.Axis(tickMinStep=1))
        )


rd =  ReadDocument('file.txt')
print(rd.parse_file())
rd.bar_chart_plot()
