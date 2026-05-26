electricity=int(input("enter the consumption of electricity: "))
if electricity<50:
    cost_per_unit=2.60
    tax=25
    bill=electricity*cost_per_unit
    total_bill=bill+tax
    print(total_bill)
elif electricity >50 and electricity<100:
    cost_per_unit=3.25
    tax=35
    bill=electricity*cost_per_unit
    total_bill=bill+tax
    print(total_bill)
elif electricity >100 and electricity<200:
    cost_per_unit=5.26
    tax=45
    bill=electricity*cost_per_unit
    total_bill=bill+tax
    print(total_bill)
else:
    cost_per_unit=8.45
    tax=75
    bill=electricity*cost_per_unit
    total_bill=bill+tax
    print(total_bill)