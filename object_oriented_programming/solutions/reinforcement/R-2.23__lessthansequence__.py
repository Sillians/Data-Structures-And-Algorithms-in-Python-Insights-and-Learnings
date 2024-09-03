from object_oriented_programming.abstract_base_classes.sequence import Sequence
import inspect

class LessThanSequence(Sequence):

    def __init__(self, sequence_value: list):
        self._sequence_value = sequence_value

    def __len__(self):
        return len(self._sequence_value)

    def __getitem__(self, item):
        return self._sequence_value[item]

    def __lt__(self, other):
        if isinstance(other, LessThanSequence):
            return self._sequence_value < other._sequence_value
        return False

    # def __lt__(self, j, k):
    #     return j < k

seq_values = [8, 3, 4, 2, 6, 7, 8]
seq2_values = [3, 4, 5, 6, 7, 4, 5]
seq1 = LessThanSequence(seq_values)
seq2 = LessThanSequence(seq2_values)
print(seq1[4] < seq2[3])