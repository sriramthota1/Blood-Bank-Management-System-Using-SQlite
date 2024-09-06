from main.conduct_pack import owner_input as o
from main.conduct_pack import eligibility as e
from main.conduct_pack import owner_login as ol
from main.conduct_pack import details_b_q as dl
from main.conduct_pack import registrations_no as r

while True:

    print('''
        1.donor application
        2.check the eligibility of donors for donating blood 
        3.fetch the details of blood grp and quantity
        4.owner login to fetch the details based on  blood group 
        5.number of registrations and values of all registrations
        6.exit                                                            
        ''' )
    print("Choose any option above")
    ch=int(input())
    if ch == 1:
         print("insert the details of donor application")
         o.donor_app()
         print("_________________________________________________________________")

    elif ch == 2:
         num=input("enter donor number:")
         qty = input("enter amount of quantity of blood donating")
         e.ck_eli(num,qty)
         print("_________________________________________________________________")

    elif ch == 3:
        blg=input("enter blood group(blood group format-(ab+))")
        dl.get_det(blg.lower())
        print("_________________________________________________________________")

    elif ch == 4:
        bg = input("enter blood group")
        b=bg.lower()
        ol.owner_lg(b)
        print("_________________________________________________________________")

    elif ch==5:
         r.regis_n()
         print("_________________________________________________________________")
    else:
        break
