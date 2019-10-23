import unittest

from sequence import Sequence


class SequenceTestCase(unittest.TestCase):

    def test_get_nucleotides(self):
        sequence_str = "GATTACCA"
        sequence = Sequence(sequence_str)
        self.assertEqual(sequence_str, sequence.nucleotides,
                         msg="Nucleotides returned were not those given")

    def test_get_weight(self):
        sequence = Sequence("G")
        self.assertAlmostEqual(Sequence.WEIGHTS['G'],
                               sequence.get_weight(),
                               delta=0.01,
                               msg="Weight returned was unexpected")

    def test_calculate_weight(self):
        sequence = Sequence("G")
        self.assertAlmostEqual(Sequence.WEIGHTS['G'],
                               Sequence.calculate_weight(sequence),
                               delta=0.01,
                               msg="Weight returned was unexpected")

    def test_nucleotides(self):
        sequence = Sequence("gtcgtcca")
        self.assertEqual('GTCGTCCA', sequence.nucleotides,
                         msg="Nucleotides returned were not those given")

    def test_get_weight_empty(self):
        sequence = Sequence("")
        self.assertAlmostEqual(0.0,
                               sequence.get_weight(),
                               delta=0.01,
                               msg="Weight returned was unexpected")

    def test_sequence_acgtx(self):
        with self.assertRaises(AssertionError):
            Sequence("ACGTX")

    def test_complement(self):
        sequence = Sequence("GATTACCA")
        print(sequence.complement)
        msgout = sequence.complement
        self.assertEqual("CTAATGGT", sequence.complement,
                         msg = "hhh")
