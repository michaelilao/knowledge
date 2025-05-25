# Car Rental System OOD

## Requirements
- Allow customers to browse and reserve car for specific dates
- Each car should have a make, model, license plate and price
- Allow for search on various criteria, type, price range, avaiability
- System should handle reservations, creating, modifying and cancelling reservations
- Track of availability of cars and handle their status accordingly
- Customer Information, name, details, license information, contact


## Classes

### Car

#### Properties
- CarId
- Make (Ford, Mazda, BMW)
- Type (SUV, Sedan, Truck)
- LicencePlate
- PricePerDay

### Reservation
- Id
- CarId
- StartDate
- EndDate

#### Methods
- ChangeReservationDates(startDate, endDate)


### Rental System
#### Properties
- Cars[]
- Reservation[]

#### Methods
- AddCar(car)
- RemoveCar(carId)
- SearchCars(startDate, endDate, carMake, carType, priceLow, priceHigh)
- CreateReservation(CarId, Customer, startDate, endDate)
- CancelReservation(reservationId)
- ModifyReservation(reservationId, startDate, endDate)
- IsAvailable(carId, startDate, endDate)





