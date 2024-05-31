from statistics import mode

class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise ValueError("Cannot change name.")
        elif isinstance(name, str) and 3 <= len(name):
            self._name = name
        else:
            raise ValueError("Name must be a str greater than or equal to 3 characters.")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        unique_visitors = []
        for trip in Trip.all:
            if trip.national_park == self and trip.visitor not in unique_visitors:
                unique_visitors.append(trip.visitor)
        return unique_visitors
    
    def total_visits(self):
        count = 0
        for trip in Trip.all:
            if trip.national_park == self:
                count += 1
        return count
    
    def best_visitor(self):
        visitors = []
        for trip in Trip.all:
            if trip.national_park == self:
                visitors.append(trip.visitor)
        return mode(visitors)


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise ValueError("Visitor must be an instance of the visitor class.")

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise ValueError("National Park should be an instance of the NationalPark class.")

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and 7 <= len(start_date):
            self._start_date = start_date
        else:
            raise ValueError("Start date should be a str greater than or equal to 7 characters.")

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and 7 <= len(end_date):
            self._end_date = end_date
        else:
            raise ValueError("End date should be a str greater than or equal to 7 characters.")
        
class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("name should be a str between 1 and 15 characters")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        unique_parks = []
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park not in unique_parks:
                unique_parks.append(trip.national_park)
        return unique_parks
    
    def total_visits_at_park(self, park):
        count = 0
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park == park:
                count += 1
        return count
