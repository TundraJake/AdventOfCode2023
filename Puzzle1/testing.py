import unittest
from main import ExtractNumberInRow, SumFirstAndLastDigits

class TestExtraction(unittest.TestCase):

    def test_extraction(self):
        self.assertEqual(ExtractNumberInRow("sesix"), "6")
        self.assertEqual(ExtractNumberInRow("nnineeight"), "98")
        self.assertEqual(ExtractNumberInRow("nnineight"), "9")
        self.assertEqual(ExtractNumberInRow("gxhtwo17fourtjkgpbhxn3five"), "217435")
        self.assertEqual(ExtractNumberInRow("225fivethtwo"), "22552")
        self.assertEqual(ExtractNumberInRow("xcbvcdfg2edfg43four"), "2434")
        self.assertEqual(ExtractNumberInRow("1seveneightone1"), "17811")
        self.assertEqual(ExtractNumberInRow("1seveneightone1"), "17811")
        self.assertEqual(ExtractNumberInRow("111"), "111")
        self.assertEqual(ExtractNumberInRow("69"), "69")
        self.assertEqual(ExtractNumberInRow("6one9"), "619")
        self.assertEqual(ExtractNumberInRow("nnnnnnnone"), "1")
        self.assertEqual(ExtractNumberInRow("nnnnnnnine"), "9")
        self.assertEqual(ExtractNumberInRow("nnnnnnnine1"), "91")
        self.assertEqual(ExtractNumberInRow("nnnnnnnone1"), "11")
        self.assertEqual(ExtractNumberInRow("seveseven"), "7")
        self.assertEqual(ExtractNumberInRow("two1nine"), "219")
        self.assertEqual(ExtractNumberInRow("eightwothree"), "83")
        self.assertEqual(ExtractNumberInRow("abcone2threexyz"), "123")
        self.assertEqual(ExtractNumberInRow("xtwone3four"), "234")
        self.assertEqual(ExtractNumberInRow("4nineeightseven2"), "49872")
        self.assertEqual(ExtractNumberInRow("zoneight234"), "1234")
        self.assertEqual(ExtractNumberInRow("7pqrstsixteen"), "76")
        self.assertEqual(ExtractNumberInRow("fbbdeightzzsdffh8jbjzxkclj"), "88")
        self.assertEqual(ExtractNumberInRow("eightfblzpmhs4"), "84")
        self.assertEqual(ExtractNumberInRow("pseven3threeeightseven"), "73387")
        self.assertEqual(ExtractNumberInRow("16fivetwo"), "1652")
        self.assertEqual(ExtractNumberInRow("oneight"), "1")
        self.assertEqual(ExtractNumberInRow("eightone"), "81")
        self.assertEqual(ExtractNumberInRow("151"), "151")
        self.assertEqual(ExtractNumberInRow("1"), "1")
        self.assertEqual(ExtractNumberInRow("three456three456fourninetwoseven"), "345634564927")
        self.assertEqual(ExtractNumberInRow("sixteen"), "6")
        self.assertEqual(ExtractNumberInRow("6798one3sixjfive"), "67981365")
        self.assertEqual(ExtractNumberInRow("dbtrsnscpztworfgdjrctwo2one9"), "22219")
        self.assertEqual(ExtractNumberInRow("twone"), "2")
        self.assertEqual(ExtractNumberInRow("twoone"), "21")
        self.assertEqual(ExtractNumberInRow("eighteight"), "88")
        self.assertEqual(ExtractNumberInRow("eightnine"), "89")
        self.assertEqual(ExtractNumberInRow("v4"), "4")
        self.assertEqual(ExtractNumberInRow("nnnn4"), "4")
        self.assertEqual(ExtractNumberInRow("nnnnin4"), "4")
        self.assertEqual(ExtractNumberInRow("nnnnin45678ne1234"), "456781234")
        self.assertEqual(ExtractNumberInRow("threone"), "1")
        self.assertEqual(ExtractNumberInRow("threontwo"), "2")
        self.assertEqual(ExtractNumberInRow("threon45two"), "452")
        self.assertEqual(ExtractNumberInRow("oneightethreon45two"), "1452")
        self.assertEqual(ExtractNumberInRow("threeeight3"), "383")
        self.assertEqual(ExtractNumberInRow("t1vcttwo"), "12")
        self.assertEqual(ExtractNumberInRow("oneight"), "18")


    def test_sumList(self):
        numbersList = ["6"]
        self.assertEqual(SumFirstAndLastDigits(numbersList), 66)
        numbersList = ["6", "12"]
        self.assertEqual(SumFirstAndLastDigits(numbersList), 78)
        numbersList = ["6", "12", "25345"]
        self.assertEqual(SumFirstAndLastDigits(numbersList), 103)
        numbersList = ["6", "12", "25345", "11"]
        self.assertEqual(SumFirstAndLastDigits(numbersList), 114)


def RunTests():
    unittest.main()

RunTests()