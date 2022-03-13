from Domain.activitate_arare_validator import ActivitateArareValidator
from Domain.tractor_validator import TractorValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.activitate_arare_service import ActivitateArareService
from Service.tractor_service import TractorService
from UserInterface.Console import Console


def main():
    truck_validator = TractorValidator()
    truck_repository = GenericFileRepository("trucks.txt")
    agricultural_activity_repository = GenericFileRepository("agricultural_activitys.txt")
    truck_service = TractorService(truck_repository, truck_validator, agricultural_activity_repository)
    agricultural_activity_validator = ActivitateArareValidator()
    agricultural_activity_service = ActivitateArareService(agricultural_activity_repository,
                                                           agricultural_activity_validator, truck_repository)
    console = Console(truck_service, agricultural_activity_service)
    console.run_console()


main()
