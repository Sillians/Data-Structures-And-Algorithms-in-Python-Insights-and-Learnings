#The collections.Sequence abstract base class does not provide support for comparing two sequences to each other.
# Modify our Sequence class from Code Fragment 2.14 to include a deﬁnition for the eq method, so that expression
# seq1 == seq2 will return True precisely when the two sequences are element by element equivalent.

from object_oriented_programming.abstract_base_classes.sequence import Sequence

class SequenceComparison(Sequence):
    """Our own version of collections.Sequence abstract base class."""
    def __init__(self, sequence_value: list):
        self._sequence_value = sequence_value

    def __len__(self):
        return len(self._sequence_value)

    def __getitem__(self, item):
        return self._sequence_value[item]

    # def __eq__(self, other):
    #     if isinstance(other, SequenceComparison):
    #         return self._sequence_value == other._sequence_value
    #     return False

    def __eq__(self, other):
        assert len(self._sequence_value) == len(other), "Dimension of both sequences must be the same"
        for j in range(len(self._sequence_value)):
            if self._sequence_value[j] == other[j]:
                return True
            return False


seq_values = [8, 3, 4, 2, 6, 7, 8]
seq2_values = [3, 4, 5, 6, 7, 4, 5]
seq1 = SequenceComparison(seq_values)
seq2 = SequenceComparison(seq2_values)
seq3 = SequenceComparison(seq_values)

print(seq1 == seq2)
print(seq1 == seq3)
print(len(seq2))