

class Vendor:

    def __init__(self, v_number, v_name, department, ranking):
        self.vendor_number = v_number
        self.vendor_name = v_name
        self.department = department
        self.overtime_hours = 0
        self.ranking = ranking

    def __str__(self):
        hourly_rate = self.__get_hourly_rate()
        overtime_pay = self.__calculate_overtime_pay()
        return f"Vendor Number: {self.vendor_number},\nName: {self.vendor_name},\nDepartment: {self.department},\nHourly Rate: ${hourly_rate},\nOvertime Pay: ${overtime_pay}"

    # Private method to get hourly rate based on ranking
    def __get_hourly_rate(self):
        if self.ranking == "Manager":
            return 50.0
        elif self.ranking == "Supervisor":
            return 35.0
        elif self.ranking == "Officer":
            return 20.0
        else:
            return 15.0
        
    def add_overtime(self, hours):
        if hours > 0:
            self.overtime_hours += hours
            print(f"Added {hours} overtime hours. Total overtime hours: {self.overtime_hours}.")
        else:
            print("Overtime hours must be positive.")

    def __calculate_overtime_pay(self):
        hourly_rate = self.__get_hourly_rate()
        overtime_pay = self.overtime_hours * hourly_rate
        return overtime_pay
    

vendor1 = Vendor("V1001", "Alice Smith", "Electronics", "Manager")
print("=============Vendor Details=============")
print(vendor1)
print("========================================")
print()

vendor1.add_overtime(5)

print("=============Vendor Details=============")
print(vendor1)
print("========================================")
print()

