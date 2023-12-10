from typing import Any
import os
import sys

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the script's directory
parent_dir = os.path.dirname(script_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from utils import CSVMixin, parse_csv_file_to_models  # noqa


class MunicipalityAndArea(CSVMixin):
    def __init__(
        self,
        Prefecture: str,
        MunicipalityCount: int,
        CityCount: int,
        TownCount: int,
        VillageCount: int,
        WardCount: int,
        TotalArea: float,
        PerMillage: float
    ) -> None:
        self.Prefecture = Prefecture
        self.MunicipalityCount = MunicipalityCount
        self.CityCount = CityCount
        self.TownCount = TownCount
        self.VillageCount = VillageCount
        self.WardCount = WardCount
        self.TotalArea = TotalArea
        self.PerMillage = PerMillage

    @staticmethod
    def fromCSV(csv_dict: dict[str, Any]) -> "MunicipalityAndArea":
        return MunicipalityAndArea(
            Prefecture=csv_dict["都道府県"],
            MunicipalityCount=int(csv_dict["市町村数"]),
            CityCount=int(csv_dict["市"]),
            TownCount=int(csv_dict["町"]),
            VillageCount=int(csv_dict["村"]),
            WardCount=int(csv_dict["区"]),
            TotalArea=float(csv_dict["総面積"]),
            PerMillage=float(csv_dict["千分比"]),
        )


class PopulationData(CSVMixin):
    def __init__(
        self,
        Prefecture: str,
        TotalPopulation: int,
        Age0to14: int,
        Age15to64: int,
        Age65andAbove: int,
        Age75andAbove: int
    ) -> None:
        self.Prefecture = Prefecture
        self.TotalPopulation = TotalPopulation
        self.Age0to14 = Age0to14
        self.Age15to64 = Age15to64
        self.Age65andAbove = Age65andAbove
        self.Age75andAbove = Age75andAbove

    @staticmethod
    def fromCSV(csv_dict: dict[str, Any]) -> "PopulationData":
        return PopulationData(
            Prefecture=csv_dict["都道府県"],
            TotalPopulation=int(csv_dict["総数"]),
            Age0to14=int(csv_dict["0歳から14歳"]),
            Age15to64=int(csv_dict["15歳から64歳"]),
            Age65andAbove=int(csv_dict["65歳以上"]),
            Age75andAbove=int(csv_dict["75歳以上"]),
        )


class EconomicData(CSVMixin):
    def __init__(
        self,
        Prefecture: str,
        NominalGrossPrefecturalProduct: int,
        CitizenIncome: int,
        PerCapitaIncome: int,
        RealGrossPrefecturalProduct: int,
        PrivateFinalConsumptionExpenditure: int,
        LocalGovernmentFinalConsumptionExpenditure: int,
        TotalCapital: int,
        YearOnYearIncreaseRate: float
    ):
        self.Prefecture = Prefecture
        self.NominalGrossPrefecturalProduct = NominalGrossPrefecturalProduct
        self.CitizenIncome = CitizenIncome
        self.PerCapitaIncome = PerCapitaIncome
        self.RealGrossPrefecturalProduct = RealGrossPrefecturalProduct
        self.PrivateFinalConsumptionExpenditure = PrivateFinalConsumptionExpenditure
        self.LocalGovernmentFinalConsumptionExpenditure = LocalGovernmentFinalConsumptionExpenditure
        self.TotalCapital = TotalCapital
        self.YearOnYearIncreaseRate = YearOnYearIncreaseRate

    @staticmethod
    def fromCSV(csv_dict: dict[str, Any]) -> "EconomicData":
        return EconomicData(
            Prefecture=csv_dict["都道府県"],
            NominalGrossPrefecturalProduct=int(csv_dict["名目県内総生産"]),
            CitizenIncome=int(csv_dict["県民所得"]),
            PerCapitaIncome=int(csv_dict["1人当たり県民所得"]),
            RealGrossPrefecturalProduct=int(csv_dict["実質県内総生産"]),
            PrivateFinalConsumptionExpenditure=int(csv_dict["民間最終消費支出"]),
            LocalGovernmentFinalConsumptionExpenditure=int(
                csv_dict["地方政府等最終消費支出"]),
            TotalCapital=int(csv_dict["県内総資本"]),
            YearOnYearIncreaseRate=float(csv_dict["対前年比増加率"]),
        )


municipalityAndAreaList = parse_csv_file_to_models(
    "1/市町村数と面積.csv", MunicipalityAndArea)
populationList = parse_csv_file_to_models("1/年齢区分別人口.csv", PopulationData)
economicDataList = parse_csv_file_to_models("1/県内総生産.csv", EconomicData)
