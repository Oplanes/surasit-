def read_salary(prompt="Enter salary: "):
    while True:
        try:
            s = input(prompt).strip()
            salary = float(s)
            if salary < 0:
                print("Salary must be non-negative. Try again.")
                continue
            return salary
        except ValueError:
            print("Invalid number. Try again.")

def main():
    emp_code = input("Enter employee code: ").strip()
    emp_name = input("Enter employee name: ").strip()
    salary = read_salary()

    tax = salary * 0.07
    social_security = salary * 0.03
    net_salary = salary - tax - social_security

    print("\n--- Salary Details ---")
    print(f"Employee code : {emp_code}")
    print(f"Employee name : {emp_name}")
    print(f"Gross salary  : {salary:,.2f}")
    print(f"Tax (7%)      : {tax:,.2f}")
    print(f"Social (3%)   : {social_security:,.2f}")
    print(f"Net salary    : {net_salary:,.2f}")

if __name__ == "__main__":
    main()
