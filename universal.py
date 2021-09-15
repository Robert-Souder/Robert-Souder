# Project start date: 3/23/2021
# This Version is set up for the Parts Look Up Guide laptop in BRK2 shop.
# This program has security functions for user input and import script for spreadsheet data.
# Step 1. Export xls file from Arena
# Step 2. Convert xls to xlsx file in a specific folder
# Step 3. Paste 'workable import' into code.
# Step 4. Update variable names and file path for specified file.
# *** Need to update 'workable import' with 'clean import data' script **


def cell_type(message):
    while True:
        try:
            global cell_type_input
            cell_type_input = int(input(message))
            if cell_type_input < 1:
                print("Invalid Entry")
                cell_type_input = cell_type("Choose Cell Type: ")
            elif cell_type_input > 6:
                print("Invalid Entry")
                cell_type_input = cell_type("Choose Cell Type: ")
            else:
                return cell_type_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return cell_type_input


def cell_aib_all(message):
    while True:
        try:
            global cell_aib_all_input
            cell_aib_all_input = int(input(message))
            if cell_aib_all_input < 1:
                print("Invalid Entry")
                cell_aib_all_input = cell_aib_all("Choose Cell Area: ")
            elif cell_aib_all_input > 4:
                print("Invalid Entry")
                cell_aib_all_input = cell_aib_all("Choose Cell Area: ")
            else:
                return cell_aib_all_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return cell_aib_all_input


def aib_area_depal(message):
    while True:
        try:
            global aib_area_depal_input
            aib_area_depal_input = int(input(message))
            if aib_area_depal_input < 1:
                print("Invalid Entry")
                aib_area_depal_input = aib_area_depal("Choose Cell Equipment: ")
            elif aib_area_depal_input > 9:
                print("Invalid Entry")
                aib_area_depal_input = aib_area_depal("Choose Cell Equipment: ")
            else:
                return aib_area_depal_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aib_area_depal_input


def aib_area_sing(message):
    while True:
        try:
            global aib_area_sing_input
            aib_area_sing_input = int(input(message))
            if aib_area_sing_input < 1:
                print("Invalid Entry")
                aib_area_sing_input = aib_area_sing("Choose Cell Equipment: ")
            elif aib_area_sing_input > 7:
                print("Invalid Entry")
                aib_area_sing_input = aib_area_sing("Choose Cell Equipment: ")
            else:
                return aib_area_sing_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aib_area_sing_input


def aib_sing_mattop(message):
    while True:
        try:
            global aib_sing_mattop_input
            aib_sing_mattop_input = int(input(message))
            if aib_sing_mattop_input < 1:
                print("Invalid Entry")
                aib_sing_mattop_input = aib_sing_mattop("Choose Equipment Component: ")
            elif aib_sing_mattop_input > 3:
                print("Invalid Entry")
                aib_sing_mattop_input = aib_sing_mattop("Choose Equipment Component: ")
            else:
                return aib_sing_mattop_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aib_sing_mattop_input


def aib_sing_reject(message):
    while True:
        try:
            global aib_sing_reject_input
            aib_sing_reject_input = int(input(message))
            if aib_sing_reject_input < 1:
                print("Invalid Entry")
                aib_sing_reject_input = aib_sing_reject("Choose Equipment Component: ")
            elif aib_sing_reject_input > 4:
                print("Invalid Entry")
                aib_sing_reject_input = aib_sing_reject("Choose Equipment Component: ")
            else:
                return aib_sing_reject_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aib_sing_reject_input


def aib_area_lift(message):
    while True:
        try:
            global aib_area_lift_input
            aib_area_lift_input = int(input(message))
            if aib_area_lift_input < 1:
                print("Invalid Entry")
                aib_area_lift_input = aib_area_lift("Choose Cell Equipment: ")
            elif aib_area_lift_input > 7:
                print("Invalid Entry")
                aib_area_lift_input = aib_area_lift("Choose Cell Equipment: ")
            else:
                return aib_area_lift_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aib_area_lift_input


def cell_mib_all(message):
    while True:
        try:
            global cell_mib_all_input
            cell_mib_all_input = int(input(message))
            if cell_mib_all_input < 1:
                print("Invalid Entry")
                cell_mib_all_input = cell_mib_all("Choose Cell Area: ")
            elif cell_mib_all_input > 3:
                print("Invalid Entry")
                cell_mib_all_input = cell_mib_all("Choose Cell Area: ")
            else:
                return cell_mib_all_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return cell_mib_all_input


def mib_area_adapter(message):
    while True:
        try:
            global mib_area_adapter_input
            mib_area_adapter_input = int(input(message))
            if mib_area_adapter_input < 1:
                print("Invalid Entry")
                mib_area_adapter_input = mib_area_adapter("Choose Cell Equipment: ")
            elif mib_area_adapter_input > 7:
                print("Invalid Entry")
                mib_area_adapter_input = mib_area_adapter("Choose Cell Equipment: ")
            else:
                return mib_area_adapter_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return mib_area_adapter_input


def mib_area_lift(message):
    while True:
        try:
            global mib_area_lift_input
            mib_area_lift_input = int(input(message))
            if mib_area_lift_input < 1:
                print("Invalid Entry")
                mib_area_lift_input = mib_area_lift("Choose Cell Equipment: ")
            elif mib_area_lift_input > 4:
                print("Invalid Entry")
                mib_area_lift_input = mib_area_lift("Choose Cell Equipment: ")
            else:
                return mib_area_lift_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return mib_area_lift_input


def cell_aob_all(message):
    while True:
        try:
            global cell_aob_all_input
            cell_aob_all_input = int(input(message))
            if cell_aob_all_input < 1:
                print("Invalid Entry")
                cell_aob_all_input = cell_aob_all("Choose Cell Area: ")
            elif cell_aob_all_input > 4:
                print("Invalid Entry")
                cell_aob_all_input = cell_aob_all("Choose Cell Area: ")
            else:
                return cell_aob_all_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return cell_aob_all_input


def aob_area_lower(message):
    while True:
        try:
            global aob_area_lower_input
            aob_area_lower_input = int(input(message))
            if aob_area_lower_input < 1:
                print("Invalid Entry")
                aob_area_lower_input = aob_area_lower("Choose Cell Equipment: ")
            elif aob_area_lower_input > 10:
                print("Invalid Entry")
                aob_area_lower_input = aob_area_lower("Choose Cell Equipment: ")
            else:
                return aob_area_lower_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aob_area_lower_input


def aob_area_upper(message):
    while True:
        try:
            global aob_area_upper_input
            aob_area_upper_input = int(input(message))
            if aob_area_upper_input < 1:
                print("Invalid Entry")
                aob_area_upper_input = aob_area_upper("Choose Cell Equipment: ")
            elif aob_area_upper_input > 6:
                print("Invalid Entry")
                aob_area_upper_input = aob_area_upper("Choose Cell Equipment: ")
            else:
                return aob_area_upper_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aob_area_upper_input


def aob_area_lift(message):
    while True:
        try:
            global aob_area_lift_input
            aob_area_lift_input = int(input(message))
            if aob_area_lift_input < 1:
                print("Invalid Entry")
                aob_area_lift_input = aob_area_lift("Choose Cell Equipment: ")
            elif aob_area_lift_input > 4:
                print("Invalid Entry")
                aob_area_lift_input = aob_area_lift("Choose Cell Equipment: ")
            else:
                return aob_area_lift_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return aob_area_lift_input


def cell_drain_all(message):
    while True:
        try:
            global cell_drain_all_input
            cell_drain_all_input = int(input(message))
            if cell_drain_all_input < 1:
                print("Invalid Entry")
                cell_drain_all_input = cell_drain_all("Choose Cell Area: ")
            elif cell_drain_all_input > 2:
                print("Invalid Entry")
                cell_drain_all_input = cell_drain_all("Choose Cell Area: ")
            else:
                return cell_drain_all_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return cell_drain_all_input


def drain_area_adapter(message):
    while True:
        try:
            global drain_area_adapter_input
            drain_area_adapter_input = int(input(message))
            if drain_area_adapter_input < 1:
                print("Invalid Entry")
                drain_area_adapter_input = drain_area_adapter("Choose Cell Equipment: ")
            elif drain_area_adapter_input > 3:
                print("Invalid Entry")
                drain_area_adapter_input = drain_area_adapter("Choose Cell Equipment: ")
            else:
                return drain_area_adapter_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return drain_area_adapter_input


def cell_flib_all(message):
    while True:
        try:
            global cell_flib_all_input
            cell_flib_all_input = int(input(message))
            if cell_flib_all_input < 1:
                print("Invalid Entry")
                cell_flib_all_input = cell_flib_all("Choose Cell Area: ")
            elif cell_flib_all_input > 13:
                print("Invalid Entry")
                cell_flib_all_input = cell_flib_all("Choose Cell Area: ")
            else:
                return cell_flib_all_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return cell_flib_all_input


def flib_area_reject(message):
    while True:
        try:
            global flib_area_reject_input
            flib_area_reject_input = int(input(message))
            if flib_area_reject_input < 1:
                print("Invalid Entry")
                flib_area_reject_input = flib_area_reject("Choose Cell Equipment: ")
            elif flib_area_reject_input > 6:
                print("Invalid Entry")
                flib_area_reject_input = flib_area_reject("Choose Cell Equipment: ")
            else:
                return flib_area_reject_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return flib_area_reject_input


def bot_area_all(message):
    while True:
        try:
            global bot_area_all_input
            bot_area_all_input = int(input(message))
            if bot_area_all_input < 1:
                print("Invalid Entry")
                bot_area_all_input = bot_area_all_input("Choose Equipment Component: ")
            elif bot_area_all_input > 3:
                print("Invalid Entry")
                bot_area_all_input = bot_area_all_input("Choose Equipment Component: ")
            else:
                return bot_area_all_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return bot_area_all_input


def drain_adapter_roller(message):
    while True:
        try:
            global drain_adapter_roller_input
            drain_adapter_roller_input = int(input(message))
            if drain_adapter_roller_input < 1:
                print("Invalid Entry")
                drain_adapter_roller_input = drain_adapter_roller("Choose Equipment Component: ")
            elif drain_adapter_roller_input > 10:
                print("Invalid Entry")
                drain_adapter_roller_input = drain_adapter_roller("Choose Equipment Component: ")
            else:
                return drain_adapter_roller_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return drain_adapter_roller_input


def drain_adapter_diverter(message):
    while True:
        try:
            global drain_adapter_diverter_input
            drain_adapter_diverter_input = int(input(message))
            if drain_adapter_diverter_input < 1:
                print("Invalid Entry")
                drain_adapter_diverter_input = drain_adapter_diverter("Choose Equipment Component: ")
            elif drain_adapter_diverter_input > 10:
                print("Invalid Entry")
                drain_adapter_diverter_input = drain_adapter_diverter("Choose Equipment Component: ")
            else:
                return drain_adapter_diverter_input
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return drain_adapter_diverter_input


def main_back():
    print("""

            BRK 2.0 Equipment Spare Parts Reference Guide

    <<<<<<<<<<<<<<<<<<<<<<<<<<MAIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    **Simply choose a number from the list of options and hit enter**

            Equipment Top Level:
            1. Auto Inbound
            2. Manual Inbound
            3. Auto Outbound
            4. Drain Line
            5. Floor Loaded Inbound
            6. Bot X & Bot Lift

            """)
    while True:
        cell_type("What Cell Type are you working on? ")
        if cell_type_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Auto Inbound Cell Area:

            1. Depal
            2. Singulator
            3. Lift
            4. Go Back to Main

            """)
            cell_aib_all("What Cell Area are you working on? ")
            if cell_aib_all_input == 1:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>       

            AIB Depal Area Equipment:

            1. PSU
            2. Depal EOAT
            3. Mattop Conveyors
            4. Pre-Lift
            5. Slip Sheet Gantry
            6. Chain Conveyors
            7. Shuttles
            8. Depal LPA & Over-Sized Pallet Vision Systems
            9. Go Back to Auto Inbound Area Menu

            """)
                aib_area_depal("What piece of Equipment are you working on? ")
                if aib_area_depal_input == 1:
                    print("""
            AIB Pallet Stacker Unit Components Parts List:

            """)
                    print(pdtabulate_aib(psu_aib))
                if aib_area_depal_input == 2:
                    print("""
            AIB Depal EOAT Components Parts List:

            """)
                    print(pdtabulate_aib(depal_eoat_aib))
                if aib_area_depal_input == 3:
                    print("""
            AIB Mattop Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(depal_mattop_aib))
                if aib_area_depal_input == 4:
                    print("""
            AIB Pre-Lift Components Parts List:

            """)
                    print(pdtabulate_aib(prelift_aib))
                if aib_area_depal_input == 5:
                    print("""
            AIB Slip Sheet Gantry Components Parts List:

            """)
                    print(pdtabulate_aib(gantry_aib))
                if aib_area_depal_input == 6:
                    print("""
            AIB Chain Conveyors Components Parts List:

            """)
                    print(pdtabulate_aob(chain_conveyor_main))
                if aib_area_depal_input == 7:
                    print("""
            AIB Shuttle Conveyors Components:
            1. Under Construction 3/26/2021

            """)
                if aib_area_depal_input == 8:
                    print("""
            AIB Depal Vision Systems Components Parts List:

            """)
                    print(pdtabulate_aib(depal_vision_aib))
                if aib_area_depal_input == 9:
                    print(aib_back())
            if cell_aib_all_input == 2:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>        

            AIB Singulator Area Equipment:

            1. Mattop Conveyors
            2. Singulator EOAT
            3. Vision System
            4. CIS & Reject Diverter & Pickface Builder Pop-Up Gate
            5. Reject Lift & Line
            6. Case Tippers
            7. Go Back to Auto Inbound Area Menu

            """)
                aib_area_sing("What piece of Equipment are you working on? ")
                if aib_area_sing_input == 1:
                    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<MATTOP MENU>>>>>>>>>>>>>>>>>>>>>>>>>>                

            AIB Singulator Mattop Conveyor Components:

            1. Singulator Pick Mattop Conveyors
            2. Case Place Mattop Conveyors
            3. Go Back to Singulator Equipment Menu

            """)
                    aib_sing_mattop("What Components Parts List do you need? ")
                    if aib_sing_mattop_input == 1:
                        print("""
            AIB Singulator Pick Mattop Conveyor Components Parts List:

            """)
                        print(pdtabulate_aib(sing_mattop_aib))
                    if aib_sing_mattop_input == 2:
                        print("""
            AIB Singulator Case Place Mattop Components Parts List:

            """)
                        print(pdtabulate_aib(case_place_aib))
                    if aib_sing_mattop_input == 3:
                        print(sing_back())
                if aib_area_sing_input == 2:
                    print("""
            AIB Singulator EOAT Components Parts List:

            """)
                    print(pdtabulate_aib(sing_eoat_aib))
                if aib_area_sing_input == 3:
                    print("""
            AIB Vision System Components Parts List:

            """)
                    print(pdtabulate_aib(vision_aib))
                if aib_area_sing_input == 4:
                    print("""
            AIB CIS, Reject Diverter & Pickface Builder Pop-up Gate Components Parts List:

            """)
                    print(pdtabulate_aib(cis_aib))
                if aib_area_sing_input == 5:
                    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            AIB Reject Lift & Line Components:

            1. Quimarox Lifts
            2. Reject Line Over Pass
            3. Reject Accumulation Curve Conveyor
            4. Go Back to Singulator Equipment Menu

            """)
                    aib_sing_reject("What Components Parts List do you need? ")
                    if aib_sing_reject_input == 1:
                        print("""
            AIB Quimarox Lifts Components Parts List:

            """)
                        print(pdtabulate_aib(sing_lift_aib))
                    if aib_sing_reject_input == 2:
                        print("""
            AIB Reject Line Over Pass Components Parts List:

            """)
                        print(pdtabulate_aib(sing_line_aib))
                    if aib_sing_reject_input == 3:
                        print("""
            AIB Reject Accumulation Curve Conveyor Components Parts List:

            """)
                        print(pdtabulate_aib(sing_curve_aib))
                    if aib_sing_reject_input == 4:
                        print(sing_back())
                if aib_area_sing_input == 6:
                    print("""
            AIB Case Tipper Components Parts List:

            """)
                    print(pdtabulate_aib(case_tipper_aib))
                if aib_area_sing_input == 7:
                    print(aib_back())
            if cell_aib_all_input == 3:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>       

            AIB Lift Cell Area Equipment:

            1. Flow-Turn Curve Conveyor
            2. Staging Mattop Conveyors
            3. T-Bot 90deg Diverter
            4. P&D - Pick-Up & Delivery Conveyor
            5. LHD - Load Handling Device
            6. Lift Assembly
            7. Go Back to Auto Inbound Area Menu

            """)
                aib_area_lift("What piece of Equipment are you working on? ")
                if aib_area_lift_input == 1:
                    print("""
            AIB Flow-Turn Curve Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(lift_curve_aib))
                if aib_area_lift_input == 2:
                    print("""
            AIB Staging Mattop Conveyors Components Parts List:

            """)
                    print(pdtabulate_aib(lift_mattop_aib))
                if aib_area_lift_input == 3:
                    print("""
            AIB T-Bot 90deg Diverter Components Parts List:

            """)
                    print(pdtabulate_aib(lift_diverter_aib))
                if aib_area_lift_input == 4:
                    print("""
            AIB P&D - Pick-Up & Delivery Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(lift_pnd_main))
                if aib_area_lift_input == 5:
                    print("""
            AIB LHD - Load Handling Device Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lhd_main))
                if aib_area_lift_input == 6:
                    print("""
            AIB Lift Assembly Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lift_main))
                if aib_area_lift_input == 7:
                    print(aib_back())
            if cell_aib_all_input == 4:
                print(main_back())
        if cell_type_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Manual Inbound Cell Area:

            1. Adapter
            2. Lift Cell
            3. Go Back to Main

            """)
            cell_mib_all("What Cell Area are you working on? ")
            if cell_mib_all_input == 1:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            MIB Adapter Area Equipment:

            1. Pallet Turner
            2. Mettler Toledo Check Weigher
            3. CIS, Conveyors & Diverter
            4. Reject Line Printer
            5. Gebhardt Incline & Belt Conveyors
            6. Case Place Mattop Conveyors
            7. Go Back to Manual Inbound Area Menu

            """)
                mib_area_adapter("What piece of Equipment are you working on? ")
                if mib_area_adapter_input == 1:
                    print("""
            MIB Pallet Turner Components Parts List:
            1. Under Construction 3/28/2021

            """)
                if mib_area_adapter_input == 2:
                    print("""
            MIB Mettler Toledo Check Weigher Components Parts List:

            """)
                    print(pdtabulate_mib(check_weigher_main))
                if mib_area_adapter_input == 3:
                    print("""
            MIB CIS, Conveyors & Diverter Components Parts List:

            """)
                    print(pdtabulate_mib(cis_mib))
                if mib_area_adapter_input == 4:
                    print("""
            MIB Reject Line Printer Components:

            """)
                    print(pdtabulate_mib(reject_mib))
                if mib_area_adapter_input == 5:
                    print("""
            MIB Gebhardt Incline & Belt Conveyors Components Parts List:

            """)
                    print(pdtabulate_mib(incline_mib))
                if mib_area_adapter_input == 6:
                    print("""
            MIB Case Place Mattop Conveyors Components Parts List:

            """)
                    print(pdtabulate_mib(case_place_mib))
                if mib_area_adapter_input == 7:
                    print(mib_back())
            if cell_mib_all_input == 2:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            MIB Lift Cell Area Equipment:

            1. P&D - Pick-Up & Delivery Conveyor
            2. LHD - Load Handling Device
            3. Lift Assembly
            4. Go Back to Manual Inbound Area Menu

            """)
                mib_area_lift("What piece of Equipment are you working on? ")
                if mib_area_lift_input == 1:
                    print("""
            MIB P&D - Pick-Up & Delivery Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(lift_pnd_main))
                if mib_area_lift_input == 2:
                    print("""
            MIB LHD - Load Handling Device Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lhd_main))
                if mib_area_lift_input == 3:
                    print("""
            MIB Lift Assembly Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lift_main))
                if mib_area_lift_input == 4:
                    print(mib_back())
            if cell_mib_all_input == 3:
                print(main_back())
        if cell_type_input == 3:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Auto Outbound Cell Area:

            1. Lower Level
            2. Upper Level
            3. Lift Cell
            4. Go Back to Main

            """)
            cell_aob_all("What Cell Area are you working on? ")
            if cell_aob_all_input == 1:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Lower Level Area Equipment:

            1. Chain Conveyors
            2. P&A - Print and Apply
            3. Post-Lift
            4. FPL - Full Pallet Lift
            5. Ring Wrapper
            6. EPL - Empty Pallet Lift
            7. PDU - Pallet Dispensing Unit
            8. Shuttle Conveyor
            9. Empty Pallet Vision System
            10. Go Back to Outbound Area Menu

            """)
                aob_area_lower("What piece of Equipment are you working on? ")
                if aob_area_lower_input == 1:
                    print("""
            AOB Chain Conveyors Components Parts List:

            """)
                    print(pdtabulate_aob(chain_conveyor_main))
                if aob_area_lower_input == 2:
                    print("""
            AOB P&A - Print and Apply Components Parts List:

            """)
                    print(pdtabulate_aob(pna_aob))
                if aob_area_lower_input == 3:
                    print("""
            AOB Post-Lift Components Parts List:

            """)
                    print(pdtabulate_aob(postlift_aob))
                if aob_area_lower_input == 4:
                    print("""
            AOB FPL - Full Pallet Lift Components Parts List:

            """)
                    print(pdtabulate_aob(fpl_aob))
                if aob_area_lower_input == 5:
                    print("""
            AOB Ring Wrapper Components Parts List:

            """)
                    print(pdtabulate_aob(ring_aob))
                if aob_area_lower_input == 6:
                    print("""
            AOB EPL - Empty Pallet Lift Components Parts List:

            """)
                    print(pdtabulate_aob(epl_aob))
                if aob_area_lower_input == 7:
                    print("""
            AOB PDU - Pallet Dispensing Unit Components Parts List:

            """)
                    print(pdtabulate_aob(pdu_aob))
                if aob_area_lower_input == 8:
                    print("""
            AOB Shuttle Conveyor Components:
            1. Under Construction 3/28/2021

            """)
                if aob_area_lower_input == 9:
                    print("""
            AOB Empty Pallet Vision System Components Parts List:

            """)
                    print(pdtabulate_aob(lower_vis_aob))
                if aob_area_lower_input == 10:
                    print(aob_back())
            if cell_aob_all_input == 2:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Upper Level Area Equipment:

            1. ABB Robot & ROP EOAT
            2. Case Feed & Turner Conveyors
            3. Vision System
            4. Case Snuggers & Print & Apply
            5. Gebhardt Merge & Transfer Conveyors
            6. Go Back to Outbound Area Menu

            """)
                aob_area_upper("What piece of Equipment are you working on? ")
                if aob_area_upper_input == 1:
                    print("""
            AOB ABB Robot & ROP EOAT Components Parts List:

            """)
                    print(pdtabulate_aob(robots_aob))
                if aob_area_upper_input == 2:
                    print("""
            AOB Case Feed & Turner Conveyors Components Parts List:

            """)
                    print(pdtabulate_aob(case_feed_aob))
                if aob_area_upper_input == 3:
                    print("""
            AOB Vision System Components Parts List: 

            """)
                    print(pdtabulate_aob(vision_aob))
                if aob_area_upper_input == 4:
                    print("""
            AOB Case Snuggers & Print & Apply Components Parts List:

            """)
                    print(pdtabulate_aob(case_pna_aob))
                if aob_area_upper_input == 5:
                    print("""
            AOB Gebhardt Merge & Transfer Conveyors Components Parts List:

            """)
                    print(pdtabulate_aob(merge_aob))
                if aob_area_upper_input == 6:
                    print(aob_back())
            if cell_aob_all_input == 3:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Lift Cell Area Equipment:

            1. P&D - Pick-Up & Delivery Conveyor
            2. LHD - Load Handling Device
            3. Lift Assembly
            4. Go Back to Outbound Area Menu

            """)
                aob_area_lift("What piece of Equipment are you working on? ")
                if aob_area_lift_input == 1:
                    print("""
            AOB P&D - Pick-Up & Delivery Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(lift_pnd_main))
                if aob_area_lift_input == 2:
                    print("""
            AOB LHD - Load Handling Device Components Parts List:

            """)
                    print(pdtabulate_aob(lift_lhd_aob))
                if aob_area_lift_input == 3:
                    print("""
            AOB Lift Assembly Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lift_main))
                if aob_area_lift_input == 4:
                    print(aob_back())
            if cell_aob_all_input == 4:
                print(main_back())
        if cell_type_input == 4:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Drain Line Cell Area:

            1. Adapter
            2. Go Back to Main

            """)
            cell_drain_all("What Cell Area are you working on? ")
            if cell_drain_all_input == 1:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Drain Line Adapter Area Equipment:

            1. Decline and Belt Conveyors
            2. Roller Conveyors
            3. Diverter

            """)
                drain_area_adapter("What piece of Equipment are you working on? ")
                if drain_area_adapter_input == 1:
                    print("""
            Drain Line Decline and Belt Conveyor Components Parts List:

            """)
                    print(pdtabulate_mib(incline_mib))
                if drain_area_adapter_input == 2:
                    print("""
            Drain Line Roller Conveyor Components:
            1. Under Construction 3/28/2021

            """)
                    drain_adapter_roller("What Components Parts List do you need? ")
                    if drain_adapter_roller_input == 1:
                        print("""
            1. Under Construction 3/28/2021

            """)
                if drain_area_adapter_input == 3:
                    print("""
            Drain Line Diverter Components:
            1. Under Construction 3/28/2021

            """)
                    drain_adapter_diverter("What Components Parts List do you need? ")
                    if drain_adapter_diverter_input == 1:
                        print("""
            1. Under Construction 3/28/2021

            """)
            if cell_drain_all_input == 2:
                print(main_back())
        if cell_type_input == 5:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Floor Loaded Inbound Cell Equipment:

            1. SRS Telescoping Conveyor
            2. Over-sized Carton Detection System (GAC)
            3. Gebhardt Infeed Conveyors
            4. Justification Table
            5. Case Centering Snugger
            6. CIS & Open Flap Detection System
            7. Haz-mat Detection System
            8. Bar Code Reader Tunnel
            9. Case Turner
            10. Half Snugger
            11. Reject Lines
            12. Lift Cell
            13. Go Back to Main

            """)
            cell_flib_all(" What piece of Equipment are you working on? ")
            if cell_flib_all_input == 1:
                print("""
            FLIB SRS Telescoping Conveyor Components Parts List:

            """)
                print(pdtabulate_flib(flib_srs))
            if cell_flib_all_input == 2:
                print("""
            FLIB Over-sized Carton Detection System (GAC) Components Parts List:

            """)
                print(pdtabulate_flib(flib_gak))
            if cell_flib_all_input == 3:
                print("""
            FLIB Gebhardt Infeed Conveyors Components Parts List:

            """)
                print(pdtabulate_flib(flib_gebhardt))
            if cell_flib_all_input == 4:
                print("""
            FLIB Justification Table Components Parts List:

            """)
                print(pdtabulate_flib(flib_justification))
            if cell_flib_all_input == 5:
                print("""
            FLIB Case Centering Snugger Components Parts List:

            """)
                print(pdtabulate_flib(flib_centering))
            if cell_flib_all_input == 6:
                print("""
            FLIB CIS & Open Flap Detection System Components Parts List:

            """)
                print(pdtabulate_flib(flib_cis))
            if cell_flib_all_input == 7:
                print("""
            FLIB Haz-mat Detection System Components Parts List:

            """)
                print(pdtabulate_flib(flib_hazmat))
            if cell_flib_all_input == 8:
                print("""
            FLIB Bar Code Reader Tunnel Components Parts List:

            """)
                print(pdtabulate_flib(flib_bcr))
            if cell_flib_all_input == 9:
                print("""
            FLIB Case Turner Components Parts List:

            """)
                print(pdtabulate_flib(flib_turner))
            if cell_flib_all_input == 10:
                print("""
            FLIB Half Snugger Components Parts List:

            """)
                print(pdtabulate_flib(flib_snugger))
            if cell_flib_all_input == 11:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            FLIB Reject Lines Equipment:

            1. Reject Accumulation Conveyors
            2. Reject Line Conveyors
            3. Reversible Reject Conveyors
            4. Print & Apply Reject Line
            5. Ball Transfer Table
            6. Go Back to FLIB Equipment Menu
            """)
                flib_area_reject("What Components Parts List do you need? ")
                if flib_area_reject_input == 1:
                    print("""
            Reject Accumulation Conveyors Components Parts List:

            """)
                    print(pdtabulate_flib(flib_accum))
                if flib_area_reject_input == 2:
                    print("""
            Reject Line Conveyors Components Parts List:

            """)
                    print(pdtabulate_flib(flib_reject))
                if flib_area_reject_input == 3:
                    print("""
            Reversible Reject Conveyors Components Parts List:

            """)
                    print(pdtabulate_flib(flib_reverse))
                if flib_area_reject_input == 4:
                    print("""
            Print & Apply Reject Line Components Parts List:

            """)
                    print(pdtabulate_flib(flib_pna))
                if flib_area_reject_input == 5:
                    print("""
            Ball Transfer Table Conponents Parts List:

            """)
                    print(pdtabulate_flib(flib_ball))
                if flib_area_reject_input == 6:
                    print(flib_back())
            if cell_flib_all_input == 12:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<LIFT CELL MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            FLIB Lift Cell Equipment:

            1. Pick-up & Delivery Conveyor
            2. Load Handling Device
            3. Lift Assembly
            4. Go Back to FLIB Equipment Menu

            """)
                mib_area_lift("What piece of Equipment are you working on?")
                if mib_area_lift_input == 1:
                    print("""
            FLIB Pick-Up & Delivery Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(lift_pnd_main))
                if mib_area_lift_input == 2:
                    print("""
            FLIB Load Handling Device Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lhd_main))
                if mib_area_lift_input == 3:
                    print("""
            FLIB Lift Assembly Components Parts List:

            """)
                    print(pdtabulate_aib(lift_lift_main))
                if mib_area_lift_input == 4:
                    print(flib_back())
            if cell_flib_all_input == 13:
                print(main_back())
        if cell_type_input == 6:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Bot X & Bot Lift:

            1. Bot X
            2. Bot Lift
            3. Go Back to Main

            """)
            bot_area_all("What piece of Equipment are you working on? ")
            if bot_area_all_input == 1:
                print("""
            Bot X Components Parts List:            

            """)
                print(pdtabulate_bot(bot_x_main))
            if bot_area_all_input == 2:
                print("""
            Bot Lift Components Parts List:

            """)
                print(pdtabulate_bot(bot_lift_main))
            if bot_area_all_input == 3:
                print(main_back())
        break


def aib_back():
    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Auto Inbound Cell Area:

            1. Depal
            2. Singulator
            3. Lift
            4. Go Back to Main

        """)
    while True:
        cell_aib_all("What Cell Area are you working on? ")
        if cell_aib_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>       

            AIB Depal Area Equipment:

            1. PSU
            2. Depal EOAT
            3. Mattop Conveyors
            4. Pre-Lift
            5. Slip Sheet Gantry
            6. Chain Conveyors
            7. Shuttles
            8. Depal LPA & Over-Sized Pallet Vision Systems
            9. Go Back to Auto Inbound Area Menu

            """)
            aib_area_depal("What piece of Equipment are you working on? ")
            if aib_area_depal_input == 1:
                print("""
            AIB Pallet Stacker Unit Components Parts List:

            """)
                print(pdtabulate_aib(psu_aib))
            if aib_area_depal_input == 2:
                print("""
            AIB Depal EOAT Components Parts List:

            """)
                print(pdtabulate_aib(depal_eoat_aib))
            if aib_area_depal_input == 3:
                print("""
            AIB Mattop Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(depal_mattop_aib))
            if aib_area_depal_input == 4:
                print("""
            AIB Pre-Lift Components Parts List:

            """)
                print(pdtabulate_aib(prelift_aib))
            if aib_area_depal_input == 5:
                print("""
            AIB Slip Sheet Gantry Components Parts List:

            """)
                print(pdtabulate_aib(gantry_aib))
            if aib_area_depal_input == 6:
                print("""
            AIB Chain Conveyors Components Parts List:

            """)
                print(pdtabulate_aob(chain_conveyor_main))
            if aib_area_depal_input == 7:
                print("""
            AIB Shuttle Conveyors Components:
            1. Under Construction 3/26/2021

            """)
            if aib_area_depal_input == 8:
                print("""
            AIB Depal Vision Systems Components Parts List:

            """)
                print(pdtabulate_aib(depal_vision_aib))
            if aib_area_depal_input == 9:
                print(aib_back())
        if cell_aib_all_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>        

            AIB Singulator Area Equipment:

            1. Mattop Conveyors
            2. Singulator EOAT
            3. Vision System
            4. CIS & Reject Diverter & Pickface Builder Pop-Up Gate
            5. Reject Lift & Line
            6. Case Tippers
            7. Go Back to Auto Inbound Area Menu

            """)
            aib_area_sing("What piece of Equipment are you working on? ")
            if aib_area_sing_input == 1:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<MATTOP MENU>>>>>>>>>>>>>>>>>>>>>>>>>>                

            AIB Singulator Mattop Conveyor Components:

            1. Singulator Pick Mattop Conveyors
            2. Case Place Mattop Conveyors
            3. Go Back to Singulator Equipment Menu

            """)
                aib_sing_mattop("What Components Parts List do you need? ")
                if aib_sing_mattop_input == 1:
                    print("""
            AIB Singulator Pick Mattop Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(sing_mattop_aib))
                if aib_sing_mattop_input == 2:
                    print("""
            AIB Singulator Case Place Mattop Components Parts List:

            """)
                    print(pdtabulate_aib(case_place_aib))
                if aib_sing_mattop_input == 3:
                    print(sing_back())
            if aib_area_sing_input == 2:
                print("""
            AIB Singulator EOAT Components Parts List:

            """)
                print(pdtabulate_aib(sing_eoat_aib))
            if aib_area_sing_input == 3:
                print("""
            AIB Vision System Components Parts List:

            """)
                print(pdtabulate_aib(vision_aib))
            if aib_area_sing_input == 4:
                print("""
            AIB CIS, Reject Diverter & Pickface Builder Pop-up Gate Components Parts List:

            """)
                print(pdtabulate_aib(cis_aib))
            if aib_area_sing_input == 5:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            AIB Reject Lift & Line Components:

            1. Quimarox Lifts
            2. Reject Line Over Pass
            3. Reject Accumulation Curve Conveyor
            4. Go Back to Singulator Equipment Menu

            """)
                aib_sing_reject("What Components Parts List do you need? ")
                if aib_sing_reject_input == 1:
                    print("""
            AIB Quimarox Lifts Components Parts List:

            """)
                    print(pdtabulate_aib(sing_lift_aib))
                if aib_sing_reject_input == 2:
                    print("""
            AIB Reject Line Over Pass Components Parts List:

            """)
                    print(pdtabulate_aib(sing_line_aib))
                if aib_sing_reject_input == 3:
                    print("""
            AIB Reject Accumulation Curve Conveyor Components Parts List:

            """)
                    print(pdtabulate_aib(sing_curve_aib))
                if aib_sing_reject_input == 4:
                    print(sing_back())
            if aib_area_sing_input == 6:
                print("""
            AIB Case Tipper Components Parts List:

            """)
                print(pdtabulate_aib(case_tipper_aib))
            if aib_area_sing_input == 7:
                print(aib_back())
        if cell_aib_all_input == 3:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>       

            AIB Lift Cell Area Equipment:

            1. Flow-Turn Curve Conveyor
            2. Staging Mattop Conveyors
            3. T-Bot 90deg Diverter
            4. P&D - Pick-Up & Delivery Conveyor
            5. LHD - Load Handling Device
            6. Lift Assembly
            7. Go Back to Auto Inbound Area Menu

            """)
            aib_area_lift("What piece of Equipment are you working on? ")
            if aib_area_lift_input == 1:
                print("""
            AIB Flow-Turn Curve Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(lift_curve_aib))
            if aib_area_lift_input == 2:
                print("""
            AIB Staging Mattop Conveyors Components Parts List:

            """)
                print(pdtabulate_aib(lift_mattop_aib))
            if aib_area_lift_input == 3:
                print("""
            AIB T-Bot 90deg Diverter Components Parts List:

            """)
                print(pdtabulate_aib(lift_diverter_aib))
            if aib_area_lift_input == 4:
                print("""
            AIB P&D - Pick-Up & Delivery Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(lift_pnd_main))
            if aib_area_lift_input == 5:
                print("""
            AIB LHD - Load Handling Device Components Parts List:

            """)
                print(pdtabulate_aib(lift_lhd_main))
            if aib_area_lift_input == 6:
                print("""
            AIB Lift Assembly Components Parts List:

            """)
                print(pdtabulate_aib(lift_lift_main))
            if aib_area_lift_input == 7:
                print(aib_back())
        if cell_aib_all_input == 4:
            print(main_back())
        break


def sing_back():
    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>        

            AIB Singulator Area Equipment:

            1. Mattop Conveyors
            2. Singulator EOAT
            3. Vision System
            4. CIS & Reject Diverter & Pickface Builder Pop-Up Gate
            5. Reject Lift & Line
            6. Case Tippers
            7. Go Back to Auto Inbound Area Menu

        """)
    while True:
        aib_area_sing("What piece of Equipment are you working on? ")
        if aib_area_sing_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<MATTOP MENU>>>>>>>>>>>>>>>>>>>>>>>>>>                

            AIB Singulator Mattop Conveyor Components:

            1. Singulator Pick Mattop Conveyors
            2. Case Place Mattop Conveyors
            3. Go Back to Singulator Equipment Menu

            """)
            aib_sing_mattop("What Components Parts List do you need? ")
            if aib_sing_mattop_input == 1:
                print("""
            AIB Singulator Pick Mattop Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(sing_mattop_aib))
            if aib_sing_mattop_input == 2:
                print("""
            AIB Singulator Case Place Mattop Components Parts List:

            """)
                print(pdtabulate_aib(case_place_aib))
            if aib_sing_mattop_input == 3:
                print(sing_back())
        if aib_area_sing_input == 2:
            print("""
            AIB Singulator EOAT Components Parts List:

            """)
            print(pdtabulate_aib(sing_eoat_aib))
        if aib_area_sing_input == 3:
            print("""
            AIB Vision System Components Parts List:

            """)
            print(pdtabulate_aib(vision_aib))
        if aib_area_sing_input == 4:
            print("""
            AIB CIS, Reject Diverter & Pickface Builder Pop-up Gate Components Parts List:

            """)
            print(pdtabulate_aib(cis_aib))
        if aib_area_sing_input == 5:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            AIB Reject Lift & Line Components:

            1. Quimarox Lifts
            2. Reject Line Over Pass
            3. Reject Accumulation Curve Conveyor
            4. Go Back to Singulator Equipment Menu

            """)
            aib_sing_reject("What Components Parts List do you need? ")
            if aib_sing_reject_input == 1:
                print("""
            AIB Quimarox Lifts Components Parts List:

            """)
                print(pdtabulate_aib(sing_lift_aib))
            if aib_sing_reject_input == 2:
                print("""
            AIB Reject Line Over Pass Components Parts List:

            """)
                print(pdtabulate_aib(sing_line_aib))
            if aib_sing_reject_input == 3:
                print("""
            AIB Reject Accumulation Curve Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(sing_curve_aib))
            if aib_sing_reject_input == 4:
                print(sing_back())
        if aib_area_sing_input == 6:
            print("""
            AIB Case Tipper Components Parts List:

            """)
            print(pdtabulate_aib(case_tipper_aib))
        if aib_area_sing_input == 7:
            print(aib_back())
        break


def aob_back():
    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Auto Outbound Cell Area:

            1. Lower Level
            2. Upper Level
            3. Lift Cell
            4. Go Back to Main

            """)
    while True:
        cell_aob_all("What Cell Area are you working on? ")
        if cell_aob_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Lower Level Area Equipment:

            1. Chain Conveyors
            2. P&A - Print and Apply
            3. Post-Lift
            4. FPL - Full Pallet Lift
            5. Ring Wrapper
            6. EPL - Empty Pallet Lift
            7. PDU - Pallet Dispensing Unit
            8. Shuttle Conveyor
            9. Empty Pallet Vision System
            10. Go Back to Outbound Area Menu

            """)
            aob_area_lower("What piece of Equipment are you working on? ")
            if aob_area_lower_input == 1:
                print("""
            AOB Chain Conveyors Components Parts List:

            """)
                print(pdtabulate_aob(chain_conveyor_main))
            if aob_area_lower_input == 2:
                print("""
            AOB P&A - Print and Apply Components Parts List:

            """)
                print(pdtabulate_aob(pna_aob))
            if aob_area_lower_input == 3:
                print("""
            AOB Post-Lift Components Parts List:

            """)
                print(pdtabulate_aob(postlift_aob))
            if aob_area_lower_input == 4:
                print("""
            AOB FPL - Full Pallet Lift Components Parts List:

            """)
                print(pdtabulate_aob(fpl_aob))
            if aob_area_lower_input == 5:
                print("""
            AOB Ring Wrapper Components Parts List:

            """)
                print(pdtabulate_aob(ring_aob))
            if aob_area_lower_input == 6:
                print("""
            AOB EPL - Empty Pallet Lift Components Parts List:

            """)
                print(pdtabulate_aob(epl_aob))
            if aob_area_lower_input == 7:
                print("""
            AOB PDU - Pallet Dispensing Unit Components Parts List:

            """)
                print(pdtabulate_aob(pdu_aob))
            if aob_area_lower_input == 8:
                print("""
            AOB Shuttle Conveyor Components:
            1. Under Construction 3/28/2021

            """)
            if aob_area_lower_input == 9:
                print("""
            AOB Empty Pallet Vision System Components Parts List:

            """)
                print(pdtabulate_aob(lower_vis_aob))
            if aob_area_lower_input == 10:
                print(aob_back())
        if cell_aob_all_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Upper Level Area Equipment:

            1. ABB Robot & ROP EOAT
            2. Case Feed & Turner Conveyors
            3. Vision System
            4. Case Snuggers & Print & Apply
            5. Gebhardt Merge & Transfer Conveyors
            6. Go Back to Outbound Area Menu

            """)
            aob_area_upper("What piece of Equipment are you working on? ")
            if aob_area_upper_input == 1:
                print("""
            AOB ABB Robot & ROP EOAT Components Parts List:

            """)
                print(pdtabulate_aob(robots_aob))
            if aob_area_upper_input == 2:
                print("""
            AOB Case Feed & Turner Conveyors Components Parts List:

            """)
                print(pdtabulate_aob(case_feed_aob))
            if aob_area_upper_input == 3:
                print("""
            AOB Vision System Components Parts List: 

            """)
                print(pdtabulate_aob(vision_aob))
            if aob_area_upper_input == 4:
                print("""
            AOB Case Snuggers & Print & Apply Components Parts List:

            """)
                print(pdtabulate_aob(case_pna_aob))
            if aob_area_upper_input == 5:
                print("""
            AOB Gebhardt Merge & Transfer Conveyors Components Parts List:

            """)
                print(pdtabulate_aob(merge_aob))
            if aob_area_upper_input == 6:
                print(aob_back())
        if cell_aob_all_input == 3:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Lift Cell Area Equipment:

            1. P&D - Pick-Up & Delivery Conveyor
            2. LHD - Load Handling Device
            3. Lift Assembly
            4. Go Back to Outbound Area Menu

            """)
            aob_area_lift("What piece of Equipment are you working on? ")
            if aob_area_lift_input == 1:
                print("""
            AOB P&D - Pick-Up & Delivery Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(lift_pnd_main))
            if aob_area_lift_input == 2:
                print("""
            AOB LHD - Load Handling Device Components Parts List:

            """)
                print(pdtabulate_aob(lift_lhd_aob))
            if aob_area_lift_input == 3:
                print("""
            AOB Lift Assembly Components Parts List:

            """)
                print(pdtabulate_aib(lift_lift_main))
            if aob_area_lift_input == 4:
                print(aob_back())
        if cell_aob_all_input == 4:
            print(main_back())
        break


def mib_back():
    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Manual Inbound Cell Area:

            1. Adapter
            2. Lift Cell
            3. Go Back to Main

        """)
    while True:
        cell_mib_all("What Cell Area are you working on? ")
        if cell_mib_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            MIB Adapter Area Equipment:

            1. Pallet Turner
            2. Mettler Toledo Check Weigher
            3. CIS, Conveyors & Diverter
            4. Reject Line Printer
            5. Gebhardt Incline & Belt Conveyors
            6. Case Place Mattop Conveyors
            7. Go Back to Manual Inbound Area Menu

            """)
            mib_area_adapter("What piece of Equipment are you working on? ")
            if mib_area_adapter_input == 1:
                print("""
            MIB Pallet Turner Components Parts List:
            1. Under Construction 3/28/2021

            """)
            if mib_area_adapter_input == 2:
                print("""
            MIB Mettler Toledo Check Weigher Components Parts List:

            """)
                print(pdtabulate_mib(check_weigher_main))
            if mib_area_adapter_input == 3:
                print("""
            MIB CIS, Conveyors & Diverter Components Parts List:

            """)
                print(pdtabulate_mib(cis_mib))
            if mib_area_adapter_input == 4:
                print("""
            MIB Reject Line Printer Components:

            """)
                print(pdtabulate_mib(reject_mib))
            if mib_area_adapter_input == 5:
                print("""
            MIB Gebhardt Incline & Belt Conveyors Components Parts List:

            """)
                print(pdtabulate_mib(incline_mib))
            if mib_area_adapter_input == 6:
                print("""
            MIB Case Place Mattop Conveyors Components Parts List:

            """)
                print(pdtabulate_mib(case_place_mib))
            if mib_area_adapter_input == 7:
                print(mib_back())
        if cell_mib_all_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            MIB Lift Cell Area Equipment:

            1. P&D - Pick-Up & Delivery Conveyor
            2. LHD - Load Handling Device
            3. Lift Assembly
            4. Go Back to Manual Inbound Area Menu

            """)
            mib_area_lift("What piece of Equipment are you working on? ")
            if mib_area_lift_input == 1:
                print("""
            MIB P&D - Pick-Up & Delivery Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(lift_pnd_main))
            if mib_area_lift_input == 2:
                print("""
            MIB LHD - Load Handling Device Components Parts List:

            """)
                print(pdtabulate_aib(lift_lhd_main))
            if mib_area_lift_input == 3:
                print("""
            MIB Lift Assembly Components Parts List:

            """)
                print(pdtabulate_aib(lift_lift_main))
            if mib_area_lift_input == 4:
                print(mib_back())
        if cell_mib_all_input == 3:
            print(main_back())
        break


def flib_back():
    print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Floor Loaded Inbound Cell Equipment:

            1. SRS Telescoping Conveyor
            2. Over-sized Carton Detection System (GAC)
            3. Gebhardt Infeed Conveyors
            4. Justification Table
            5. Case Centering Snugger
            6. CIS & Open Flap Detection System
            7. Haz-mat Detection System
            8. Bar Code Reader Tunnel
            9. Case Turner
            10. Half Snugger
            11. Reject Lines
            12. Lift Cell
            13. Go Back to Main

        """)
    while True:
        cell_flib_all(" What piece of Equipment are you working on? ")
        if cell_flib_all_input == 1:
            print("""
            FLIB SRS Telescoping Conveyor Components Parts List:

            """)
            print(pdtabulate_flib(flib_srs))
        if cell_flib_all_input == 2:
            print("""
            FLIB Over-sized Carton Detection System (GAC) Components Parts List:

            """)
            print(pdtabulate_flib(flib_gak))
        if cell_flib_all_input == 3:
            print("""
            FLIB Gebhardt Infeed Conveyors Components Parts List:

            """)
            print(pdtabulate_flib(flib_gebhardt))
        if cell_flib_all_input == 4:
            print("""
            FLIB Justification Table Components Parts List:

            """)
            print(pdtabulate_flib(flib_justification))
        if cell_flib_all_input == 5:
            print("""
            FLIB Case Centering Snugger Components Parts List:

            """)
            print(pdtabulate_flib(flib_centering))
        if cell_flib_all_input == 6:
            print("""
            FLIB CIS & Open Flap Detection System Components Parts List:

            """)
            print(pdtabulate_flib(flib_cis))
        if cell_flib_all_input == 7:
            print("""
            FLIB Haz-mat Detection System Components Parts List:

            """)
            print(pdtabulate_flib(flib_hazmat))
        if cell_flib_all_input == 8:
            print("""
            FLIB Bar Code Reader Tunnel Components Parts List:

            """)
            print(pdtabulate_flib(flib_bcr))
        if cell_flib_all_input == 9:
            print("""
            FLIB Case Turner Components Parts List:

            """)
            print(pdtabulate_flib(flib_turner))
        if cell_flib_all_input == 10:
            print("""
            FLIB Half Snugger Components Parts List:

            """)
            print(pdtabulate_flib(flib_snugger))
        if cell_flib_all_input == 11:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            FLIB Reject Lines Equipment:

            1. Reject Accumulation Conveyors
            2. Reject Line Conveyors
            3. Reversible Reject Conveyors
            4. Print & Apply Reject Line
            5. Ball Transfer Table
            6. Go Back to FLIB Equipment Menu

            """)
            flib_area_reject("What Components Parts List do you need? ")
            if flib_area_reject_input == 1:
                print("""
            1. Reject Accumulation Conveyors Components Parts List:

            """)
                print(pdtabulate_flib(flib_accum))
            if flib_area_reject_input == 2:
                print("""
            2. Reject Line Conveyors Components Parts List:

            """)
                print(pdtabulate_flib(flib_reject))
            if flib_area_reject_input == 3:
                print("""
            3. Reversible Reject Conveyors Components Parts List:

            """)
                print(pdtabulate_flib(flib_reverse))
            if flib_area_reject_input == 4:
                print("""
            4. Print & Apply Reject Line Components Parts List:

            """)
                print(pdtabulate_flib(flib_pna))
            if flib_area_reject_input == 5:
                print("""
            5. Ball Transfer Table Conponents Parts List:

            """)
                print(pdtabulate_flib(flib_ball))
            if flib_area_reject_input == 6:
                print(flib_back())
        if cell_flib_all_input == 12:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<LIFT CELL MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            FLIB Lift Cell Equipment:

            1. Pick-up & Delivery Conveyor
            2. Load Handling Device
            3. Lift Assembly
            4. Go Back to FLIB Equipment Menu

            """)
            mib_area_lift("What piece of Equipment are you working on?")
            if mib_area_lift_input == 1:
                print("""
            FLIB Pick-Up & Delivery Conveyor Components Parts List:

            """)
                print(pdtabulate_aib(lift_pnd_main))
            if mib_area_lift_input == 2:
                print("""
            FLIB Load Handling Device Components Parts List:

            """)
                print(pdtabulate_aib(lift_lhd_main))
            if mib_area_lift_input == 3:
                print("""
            FLIB Lift Assembly Components Parts List:

            """)
                print(pdtabulate_aib(lift_lift_main))
            if mib_area_lift_input == 4:
                print(flib_back())
        if cell_flib_all_input == 13:
            print(main_back())
        break


while True:

    import pandas as pd
    from tabulate import tabulate

    pdtabulate_aib = lambda file_loc_aib: tabulate(file_loc_aib, headers='keys', tablefmt='psql')
    file_loc_aib = r"C:\Parts Look Up Guide\AIB Parts List.xlsx"
    psu_aib = pd.read_excel(file_loc_aib, sheet_name="PSU")
    depal_eoat_aib = pd.read_excel(file_loc_aib, sheet_name="Depal EOAT")
    depal_vision_aib = pd.read_excel(file_loc_aib, sheet_name="Depal Vision")
    depal_mattop_aib = pd.read_excel(file_loc_aib, sheet_name="Mattops")
    prelift_aib = pd.read_excel(file_loc_aib, sheet_name="Pre-Lift")
    gantry_aib = pd.read_excel(file_loc_aib, sheet_name="Gantry")
    sing_mattop_aib = pd.read_excel(file_loc_aib, sheet_name="Sing Pick")
    case_tipper_aib = pd.read_excel(file_loc_aib, sheet_name="Case Tipper")
    case_place_aib = pd.read_excel(file_loc_aib, sheet_name="Case Place")
    sing_eoat_aib = pd.read_excel(file_loc_aib, sheet_name="Sing EOAT")
    vision_aib = pd.read_excel(file_loc_aib, sheet_name="Vision")
    cis_aib = pd.read_excel(file_loc_aib, sheet_name="CIS")
    sing_lift_aib = pd.read_excel(file_loc_aib, sheet_name="Reject Lift")
    sing_line_aib = pd.read_excel(file_loc_aib, sheet_name="Reject Line")
    sing_curve_aib = pd.read_excel(file_loc_aib, sheet_name="Reject Curve")
    lift_curve_aib = pd.read_excel(file_loc_aib, sheet_name="Flow Turn")
    lift_mattop_aib = pd.read_excel(file_loc_aib, sheet_name="Staging Mattop")
    lift_diverter_aib = pd.read_excel(file_loc_aib, sheet_name="Diverter")
    lift_lhd_main = pd.read_excel(file_loc_aib, sheet_name="LHD")
    lift_pnd_main = pd.read_excel(file_loc_aib, sheet_name="PND")
    lift_lift_main = pd.read_excel(file_loc_aib, sheet_name="Lift")

    pdtabulate_mib = lambda file_loc_mib: tabulate(file_loc_mib, headers='keys', tablefmt='psql')
    file_loc_mib = r"C:\Parts Look Up Guide\MIB Parts List.xlsx"
    case_place_mib = pd.read_excel(file_loc_mib, sheet_name="Case Place")
    check_weigher_main = pd.read_excel(file_loc_mib, sheet_name="Weigher")
    cis_mib = pd.read_excel(file_loc_mib, sheet_name="CIS")
    incline_mib = pd.read_excel(file_loc_mib, sheet_name="Gebhardt")
    reject_mib = pd.read_excel(file_loc_mib, sheet_name="Reject")

    pdtabulate_aob = lambda file_loc_aob: tabulate(file_loc_aob, headers='keys', tablefmt='psql')
    file_loc_aob = r"C:\Parts Look Up Guide\AOB Parts List.xlsx"
    chain_conveyor_main = pd.read_excel(file_loc_aob, sheet_name="Chain")
    pna_aob = pd.read_excel(file_loc_aob, sheet_name="P&A")
    postlift_aob = pd.read_excel(file_loc_aob, sheet_name="Post-Lift")
    fpl_aob = pd.read_excel(file_loc_aob, sheet_name="FPL")
    ring_aob = pd.read_excel(file_loc_aob, sheet_name="Ring")
    epl_aob = pd.read_excel(file_loc_aob, sheet_name="EPL")
    pdu_aob = pd.read_excel(file_loc_aob, sheet_name="PDU")
    case_pna_aob = pd.read_excel(file_loc_aob, sheet_name="CC+P&A")
    robots_aob = pd.read_excel(file_loc_aob, sheet_name="Robots")
    case_feed_aob = pd.read_excel(file_loc_aob, sheet_name="Case Feed")
    vision_aob = pd.read_excel(file_loc_aob, sheet_name="Vision")
    lower_vis_aob = pd.read_excel(file_loc_aob, sheet_name="Lower Vision")
    merge_aob = pd.read_excel(file_loc_aob, sheet_name="Merge")
    lift_lhd_aob = pd.read_excel(file_loc_aob, sheet_name="LHD")

    pdtabulate_flib = lambda file_loc_flib: tabulate(file_loc_flib, headers='keys', tablefmt='psql')
    file_loc_flib = r"C:\Parts Look Up Guide\FLIB Parts List.xlsx"
    flib_srs = pd.read_excel(file_loc_flib, sheet_name="SRS Conveyor")
    flib_gak = pd.read_excel(file_loc_flib, sheet_name="GAK")
    flib_gebhardt = pd.read_excel(file_loc_flib, sheet_name="Gebhardt")
    flib_justification = pd.read_excel(file_loc_flib, sheet_name="Justification")
    flib_centering = pd.read_excel(file_loc_flib, sheet_name="Centering")
    flib_cis = pd.read_excel(file_loc_flib, sheet_name="CIS")
    flib_hazmat = pd.read_excel(file_loc_flib, sheet_name="Hazmat")
    flib_bcr = pd.read_excel(file_loc_flib, sheet_name="BCR Tunnel")
    flib_turner = pd.read_excel(file_loc_flib, sheet_name="Case Turner")
    flib_snugger = pd.read_excel(file_loc_flib, sheet_name="Half Snugger")
    flib_accum = pd.read_excel(file_loc_flib, sheet_name="Reject Accum")
    flib_reject = pd.read_excel(file_loc_flib, sheet_name="Reject Line")
    flib_reverse = pd.read_excel(file_loc_flib, sheet_name="Reverse Reject")
    flib_pna = pd.read_excel(file_loc_flib, sheet_name="P&A Reject")
    flib_ball = pd.read_excel(file_loc_flib, sheet_name="Ball Transfer")

    pdtabulate_bot = lambda file_loc_bot: tabulate(file_loc_bot, headers='keys', tablefmt='psql')
    file_loc_bot = r"C:\Parts Look Up Guide\BOT Parts List.xlsx"
    bot_x_main = pd.read_excel(file_loc_bot, sheet_name="Bot X")
    bot_lift_main = pd.read_excel(file_loc_bot, sheet_name="Bot Lift")

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.expand_frame_repr", False)
    pd.set_option("max_colwidth", None)

    print("""

            BRK 2.0 Equipment Spare Parts Reference Guide

    <<<<<<<<<<<<<<<<<<<<<<<<<<MAIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    **Simply choose a number from the list of options and hit enter**

            Equipment Top Level:
            1. Auto Inbound
            2. Manual Inbound
            3. Auto Outbound
            4. Drain Line
            5. Floor Loaded Inbound
            6. Bot X & Bot Lift

                """)
    cell_type("What Cell Type are you working on? ")
    if cell_type_input == 1:
        print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Auto Inbound Cell Area:

            1. Depal
            2. Singulator
            3. Lift
            4. Go Back to Main

                """)
    cell_aib_all("What Cell Area are you working on? ")
    if cell_aib_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>       

            AIB Depal Area Equipment:

            1. PSU
            2. Depal EOAT
            3. Mattop Conveyors
            4. Pre-Lift
            5. Slip Sheet Gantry
            6. Chain Conveyors
            7. Shuttles
            8. Depal LPA & Over-Sized Pallet Vision Systems
            9. Go Back to Auto Inbound Area Menu

                """)
            aib_area_depal("What piece of Equipment are you working on? ")
            if aib_area_depal_input == 1:
                print("""
            AIB Pallet Stacker Unit Components Parts List:

                """)
                print(pdtabulate_aib(psu_aib))
            if aib_area_depal_input == 2:
                print("""
            AIB Depal EOAT Components Parts List:

                """)
                print(pdtabulate_aib(depal_eoat_aib))
            if aib_area_depal_input == 3:
                print("""
            AIB Mattop Conveyor Components Parts List:

                """)
                print(pdtabulate_aib(depal_mattop_aib))
            if aib_area_depal_input == 4:
                print("""
            AIB Pre-Lift Components Parts List:

                """)
                print(pdtabulate_aib(prelift_aib))
            if aib_area_depal_input == 5:
                print("""
            AIB Slip Sheet Gantry Components Parts List:

                """)
                print(pdtabulate_aib(gantry_aib))
            if aib_area_depal_input == 6:
                print("""
            AIB Chain Conveyors Components Parts List:

                """)
                print(pdtabulate_aob(chain_conveyor_main))
            if aib_area_depal_input == 7:
                print("""
            AIB Shuttle Conveyors Components:
                1. Under Construction 3/26/2021

                """)
            if aib_area_depal_input == 8:
                print("""
            AIB Depal Vision Systems Components Parts List:

                """)
                print(pdtabulate_aib(depal_vision_aib))
            if aib_area_depal_input == 9:
                print(aib_back())
    if cell_aib_all_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>        

            AIB Singulator Area Equipment:

            1. Mattop Conveyors
            2. Singulator EOAT
            3. Vision System
            4. CIS & Reject Diverter & Pickface Builder Pop-Up Gate
            5. Reject Lift & Line
            6. Case Tippers
            7. Go Back to Auto Inbound Area Menu

                """)
            aib_area_sing("What piece of Equipment are you working on? ")
            if aib_area_sing_input == 1:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<MATTOP MENU>>>>>>>>>>>>>>>>>>>>>>>>>>                

            AIB Singulator Mattop Conveyor Components:

            1. Singulator Pick Mattop Conveyors
            2. Case Place Mattop Conveyors
            3. Go Back to Singulator Equipment Menu

            """)
                aib_sing_mattop("What Components Parts List do you need? ")
                if aib_sing_mattop_input == 1:
                    print("""
            AIB Singulator Pick Mattop Conveyor Components Parts List:

                """)
                    print(pdtabulate_aib(sing_mattop_aib))
                if aib_sing_mattop_input == 2:
                    print("""
            AIB Singulator Case Place Mattop Components Parts List:

                """)
                    print(pdtabulate_aib(case_place_aib))
                if aib_sing_mattop_input == 3:
                    print(sing_back())
            if aib_area_sing_input == 2:
                print("""
            AIB Singulator EOAT Components Parts List:

                """)
                print(pdtabulate_aib(sing_eoat_aib))
            if aib_area_sing_input == 3:
                print("""
            AIB Vision System Components Parts List:

                """)
                print(pdtabulate_aib(vision_aib))
            if aib_area_sing_input == 4:
                print("""
            AIB CIS, Reject Diverter & Pickface Builder Pop-up Gate Components Parts List:

                """)
                print(pdtabulate_aib(cis_aib))
            if aib_area_sing_input == 5:
                print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            AIB Reject Lift & Line Components:

            1. Quimarox Lifts
            2. Reject Line Over Pass
            3. Reject Accumulation Curve Conveyor
            4. Go Back to Singulator Equipment Menu

                """)
                aib_sing_reject("What Components Parts List do you need? ")
                if aib_sing_reject_input == 1:
                    print("""
            AIB Quimarox Lifts Components Parts List:

                """)
                    print(pdtabulate_aib(sing_lift_aib))
                if aib_sing_reject_input == 2:
                    print("""
            AIB Reject Line Over Pass Components Parts List:

                """)
                    print(pdtabulate_aib(sing_line_aib))
                if aib_sing_reject_input == 3:
                    print("""
            AIB Reject Accumulation Curve Conveyor Components Parts List:

                """)
                    print(pdtabulate_aib(sing_curve_aib))
                if aib_sing_reject_input == 4:
                    print(sing_back())
            if aib_area_sing_input == 6:
                print("""
            AIB Case Tipper Components Parts List:

                """)
                print(pdtabulate_aib(case_tipper_aib))
            if aib_area_sing_input == 7:
                print(aib_back())
    if cell_aib_all_input == 3:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>       

            AIB Lift Cell Area Equipment:

            1. Flow-Turn Curve Conveyor
            2. Staging Mattop Conveyors
            3. T-Bot 90deg Diverter
            4. P&D - Pick-Up & Delivery Conveyor
            5. LHD - Load Handling Device
            6. Lift Assembly
            7. Go Back to Auto Inbound Area Menu

                """)
            aib_area_lift("What piece of Equipment are you working on? ")
            if aib_area_lift_input == 1:
                print("""
            AIB Flow-Turn Curve Conveyor Components Parts List:

                """)
                print(pdtabulate_aib(lift_curve_aib))
            if aib_area_lift_input == 2:
                print("""
            AIB Staging Mattop Conveyors Components Parts List:

                """)
                print(pdtabulate_aib(lift_mattop_aib))
            if aib_area_lift_input == 3:
                print("""
            AIB T-Bot 90deg Diverter Components Parts List:

                """)
                print(pdtabulate_aib(lift_diverter_aib))
            if aib_area_lift_input == 4:
                print("""
            AIB P&D - Pick-Up & Delivery Conveyor Components Parts List:

                """)
                print(pdtabulate_aib(lift_pnd_main))
            if aib_area_lift_input == 5:
                print("""
            AIB LHD - Load Handling Device Components Parts List:

                """)
                print(pdtabulate_aib(lift_lhd_main))
            if aib_area_lift_input == 6:
                print("""
            AIB Lift Assembly Components Parts List:

                """)
                print(pdtabulate_aib(lift_lift_main))
            if aib_area_lift_input == 7:
                print(aib_back())
    if cell_aib_all_input == 4:
        print(main_back())
    if cell_type_input == 2:
        print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Manual Inbound Cell Area:

            1. Adapter
            2. Lift Cell
            3. Go Back to Main

                """)
        cell_mib_all("What Cell Area are you working on? ")
        if cell_mib_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            MIB Adapter Area Equipment:

            1. Pallet Turner
            2. Mettler Toledo Check Weigher
            3. CIS, Conveyors & Diverter
            4. Reject Line Printer
            5. Gebhardt Incline & Belt Conveyors
            6. Case Place Mattop Conveyors
            7. Go Back to Manual Inbound Area Menu

                """)
            mib_area_adapter("What piece of Equipment are you working on? ")
            if mib_area_adapter_input == 1:
                print("""
            MIB Pallet Turner Components Parts List:
            1. Under Construction 3/28/2021

                """)
            if mib_area_adapter_input == 2:
                print("""
            MIB Mettler Toledo Check Weigher Components Parts List:

                """)
                print(pdtabulate_mib(check_weigher_main))
            if mib_area_adapter_input == 3:
                print("""
            MIB CIS, Conveyors & Diverter Components Parts List:

                """)
                print(pdtabulate_mib(cis_mib))
            if mib_area_adapter_input == 4:
                print("""
            MIB Reject Line Printer Components:

                """)
                print(pdtabulate_mib(reject_mib))
            if mib_area_adapter_input == 5:
                print("""
            MIB Gebhardt Incline & Belt Conveyors Components Parts List:

                """)
                print(pdtabulate_mib(incline_mib))
            if mib_area_adapter_input == 6:
                print("""
            MIB Case Place Mattop Conveyors Components Parts List:

                """)
                print(pdtabulate_mib(case_place_mib))
            if mib_area_adapter_input == 7:
                print(mib_back())
        if cell_mib_all_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            MIB Lift Cell Area Equipment:

            1. P&D - Pick-Up & Delivery Conveyor
            2. LHD - Load Handling Device
            3. Lift Assembly
            4. Go Back to Manual Inbound Area Menu

                """)
            mib_area_lift("What piece of Equipment are you working on? ")
            if mib_area_lift_input == 1:
                print("""
            MIB P&D - Pick-Up & Delivery Conveyor Components Parts List:

                """)
                print(pdtabulate_aib(lift_pnd_main))
            if mib_area_lift_input == 2:
                print("""
            MIB LHD - Load Handling Device Components Parts List:

                """)
                print(pdtabulate_aib(lift_lhd_main))
            if mib_area_lift_input == 3:
                print("""
            MIB Lift Assembly Components Parts List:

                """)
                print(pdtabulate_aib(lift_lift_main))
            if mib_area_lift_input == 4:
                print(mib_back())
        if cell_mib_all_input == 3:
            print(main_back())
    if cell_type_input == 3:
        print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Auto Outbound Cell Area:

            1. Lower Level
            2. Upper Level
            3. Lift Cell
            4. Go Back to Main

                """)
        cell_aob_all("What Cell Area are you working on? ")
        if cell_aob_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Lower Level Area Equipment:

            1. Chain Conveyors
            2. P&A - Print and Apply
            3. Post-Lift
            4. FPL - Full Pallet Lift
            5. Ring Wrapper
            6. EPL - Empty Pallet Lift
            7. PDU - Pallet Dispensing Unit
            8. Shuttle Conveyor
            9. Empty Pallet Vision System
            10. Go Back to Outbound Area Menu

            """)
            aob_area_lower("What piece of Equipment are you working on? ")
            if aob_area_lower_input == 1:
                print("""
            AOB Chain Conveyors Components Parts List:

                """)
                print(pdtabulate_aob(chain_conveyor_main))
            if aob_area_lower_input == 2:
                print("""
            AOB P&A - Print and Apply Components Parts List:

                """)
                print(pdtabulate_aob(pna_aob))
            if aob_area_lower_input == 3:
                print("""
            AOB Post-Lift Components Parts List:

                """)
                print(pdtabulate_aob(postlift_aob))
            if aob_area_lower_input == 4:
                print("""
            AOB FPL - Full Pallet Lift Components Parts List:

                """)
                print(pdtabulate_aob(fpl_aob))
            if aob_area_lower_input == 5:
                print("""
            AOB Ring Wrapper Components Parts List:

                """)
                print(pdtabulate_aob(ring_aob))
            if aob_area_lower_input == 6:
                print("""
            AOB EPL - Empty Pallet Lift Components Parts List:

                """)
                print(pdtabulate_aob(epl_aob))
            if aob_area_lower_input == 7:
                print("""
            AOB PDU - Pallet Dispensing Unit Components Parts List:

                """)
                print(pdtabulate_aob(pdu_aob))
            if aob_area_lower_input == 8:
                print("""
            AOB Shuttle Conveyor Components:
            1. Under Construction 3/28/2021

                """)
            if aob_area_lower_input == 9:
                print("""
            AOB Empty Pallet Vision System Components Parts List:

                """)
                print(pdtabulate_aob(lower_vis_aob))
            if aob_area_lower_input == 10:
                print(aob_back())
        if cell_aob_all_input == 2:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Upper Level Area Equipment:

            1. ABB Robot & ROP EOAT
            2. Case Feed & Turner Conveyors
            3. Vision System
            4. Case Snuggers & Print & Apply
            5. Gebhardt Merge & Transfer Conveyors
            6. Go Back to Outbound Area Menu

                """)
            aob_area_upper("What piece of Equipment are you working on? ")
            if aob_area_upper_input == 1:
                print("""
            AOB ABB Robot & ROP EOAT Components Parts List:

                """)
                print(pdtabulate_aob(robots_aob))
            if aob_area_upper_input == 2:
                print("""
            AOB Case Feed & Turner Conveyors Components Parts List:

                """)
                print(pdtabulate_aob(case_feed_aob))
            if aob_area_upper_input == 3:
                print("""
            AOB Vision System Components Parts List: 

                """)
                print(pdtabulate_aob(vision_aob))
            if aob_area_upper_input == 4:
                print("""
            AOB Case Snuggers & Print & Apply Components Parts List:

                """)
                print(pdtabulate_aob(case_pna_aob))
            if aob_area_upper_input == 5:
                print("""
            AOB Gebhardt Merge & Transfer Conveyors Components Parts List:

                """)
                print(pdtabulate_aob(merge_aob))
            if aob_area_upper_input == 6:
                print(aob_back())
        if cell_aob_all_input == 3:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            AOB Lift Cell Area Equipment:

            1. P&D - Pick-Up & Delivery Conveyor
            2. LHD - Load Handling Device
            3. Lift Assembly
            4. Go Back to Outbound Area Menu

                """)
            aob_area_lift("What piece of Equipment are you working on? ")
            if aob_area_lift_input == 1:
                print("""
            AOB P&D - Pick-Up & Delivery Conveyor Components Parts List:

                """)
                print(pdtabulate_aib(lift_pnd_main))
            if aob_area_lift_input == 2:
                print("""
            AOB LHD - Load Handling Device Components Parts List:

                """)
                print(pdtabulate_aob(lift_lhd_aob))
            if aob_area_lift_input == 3:
                print("""
            AOB Lift Assembly Components Parts List:

                """)
                print(pdtabulate_aib(lift_lift_main))
            if aob_area_lift_input == 4:
                print(aob_back())
        if cell_aob_all_input == 4:
            print(main_back())
    if cell_type_input == 4:
        print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<AREA MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            Drain Line Cell Area:

            1. Adapter
            2. Go Back to Main

                """)
        cell_drain_all("What Cell Area are you working on? ")
        if cell_drain_all_input == 1:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Drain Line Adapter Area Equipment:

            1. Decline and Belt Conveyors
            2. Roller Conveyors
            3. Diverter

                """)
            drain_area_adapter("What piece of Equipment are you working on? ")
            if drain_area_adapter_input == 1:
                print("""
            Drain Line Decline and Belt Conveyor Components Parts List:

                """)
                print(pdtabulate_mib(incline_mib))
            if drain_area_adapter_input == 2:
                print("""
            Drain Line Roller Conveyor Components:
            1. Under Construction 3/28/2021

                """)
                drain_adapter_roller("What Components Parts List do you need? ")
                if drain_adapter_roller_input == 1:
                    print("""
            1. Under Construction 3/28/2021

                """)
            if drain_area_adapter_input == 3:
                print("""
            Drain Line Diverter Components:
            1. Under Construction 3/28/2021

                """)
                drain_adapter_diverter("What Components Parts List do you need? ")
                if drain_adapter_diverter_input == 1:
                    print("""
            1. Under Construction 3/28/2021

                """)
        if cell_drain_all_input == 2:
            print(main_back())
    if cell_type_input == 5:
        print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Floor Loaded Inbound Cell Equipment:

            1. SRS Telescoping Conveyor
            2. Over-sized Carton Detection System (GAC)
            3. Gebhardt Infeed Conveyors
            4. Justification Table
            5. Case Centering Snugger
            6. CIS & Open Flap Detection System
            7. Haz-mat Detection System
            8. Bar Code Reader Tunnel
            9. Case Turner
            10. Half Snugger
            11. Reject Lines
            12. Lift Cell
            13. Go Back to Main

                """)
        cell_flib_all(" What piece of Equipment are you working on? ")
        if cell_flib_all_input == 1:
            print("""
            FLIB SRS Telescoping Conveyor Components Parts List:

                """)
            print(pdtabulate_flib(flib_srs))
        if cell_flib_all_input == 2:
            print("""
            FLIB Over-sized Carton Detection System (GAC) Components Parts List:

                """)
            print(pdtabulate_flib(flib_gak))
        if cell_flib_all_input == 3:
            print("""
            FLIB Gebhardt Infeed Conveyors Components Parts List:

                """)
            print(pdtabulate_flib(flib_gebhardt))
        if cell_flib_all_input == 4:
            print("""
            FLIB Justification Table Components Parts List:

                """)
            print(pdtabulate_flib(flib_justification))
        if cell_flib_all_input == 5:
            print("""
            FLIB Case Centering Snugger Components Parts List:

                """)
            print(pdtabulate_flib(flib_centering))
        if cell_flib_all_input == 6:
            print("""
            FLIB CIS & Open Flap Detection System Components Parts List:

                """)
            print(pdtabulate_flib(flib_cis))
        if cell_flib_all_input == 7:
            print("""
            FLIB Haz-mat Detection System Components Parts List:

                """)
            print(pdtabulate_flib(flib_hazmat))
        if cell_flib_all_input == 8:
            print("""
            FLIB Bar Code Reader Tunnel Components Parts List:

                """)
            print(pdtabulate_flib(flib_bcr))
        if cell_flib_all_input == 9:
            print("""
            FLIB Case Turner Components Parts List:

                """)
            print(pdtabulate_flib(flib_turner))
        if cell_flib_all_input == 10:
            print("""
            FLIB Half Snugger Components Parts List:

                """)
            print(pdtabulate_flib(flib_snugger))
        if cell_flib_all_input == 11:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<<<REJECT MENU>>>>>>>>>>>>>>>>>>>>>>>>>>

            FLIB Reject Lines Equipment:

            1. Reject Accumulation Conveyors
            2. Reject Line Conveyors
            3. Reversible Reject Conveyors
            4. Print & Apply Reject Line
            5. Ball Transfer Table
            6. Go Back to FLIB Equipment Menu

                """)
            flib_area_reject("What Components Parts List do you need? ")
            if flib_area_reject_input == 1:
                print("""
            Reject Accumulation Conveyors Components Parts List:

                """)
                print(pdtabulate_flib(flib_accum))
            if flib_area_reject_input == 2:
                print("""
            Reject Line Conveyors Components Parts List:

                """)
                print(pdtabulate_flib(flib_reject))
            if flib_area_reject_input == 3:
                print("""
            Reversible Reject Conveyors Components Parts List:

                """)
                print(pdtabulate_flib(flib_reverse))
            if flib_area_reject_input == 4:
                print("""
            Print & Apply Reject Line Components Parts List:

                """)
                print(pdtabulate_flib(flib_pna))
            if flib_area_reject_input == 5:
                print("""
            Ball Transfer Table Conponents Parts List:

                """)
                print(pdtabulate_flib(flib_ball))
            if flib_area_reject_input == 6:
                print(flib_back())
        if cell_flib_all_input == 12:
            print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<LIFT CELL MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            FLIB Lift Cell Equipment:

            1. Pick-up & Delivery Conveyor
            2. Load Handling Device
            3. Lift Assembly
            4. Go Back to FLIB Equipment Menu

                """)
            mib_area_lift("What piece of Equipment are you working on?")
            if mib_area_lift_input == 1:
                print("""
            FLIB Pick-Up & Delivery Conveyor Components Parts List:

                """)
                print(pdtabulate_aib(lift_pnd_main))
            if mib_area_lift_input == 2:
                print("""
            FLIB Load Handling Device Components Parts List:

                """)
                print(pdtabulate_aib(lift_lhd_main))
            if mib_area_lift_input == 3:
                print("""
            FLIB Lift Assembly Components Parts List:

                """)
                print(pdtabulate_aib(lift_lift_main))
            if mib_area_lift_input == 4:
                print(flib_back())
        if cell_flib_all_input == 13:
            print(main_back())
    if cell_type_input == 6:
        print("""

    <<<<<<<<<<<<<<<<<<<<<<<<<EQUIPMENT MENU>>>>>>>>>>>>>>>>>>>>>>>>>

            Bot X & Bot Lift:

            1. Bot X
            2. Bot Lift
            3. Go Back to Main

                """)
        bot_area_all("What piece of Equipment are you working on? ")
        if bot_area_all_input == 1:
            print("""
            Bot X Components Parts List:            

                """)
            print(pdtabulate_bot(bot_x_main))
        if bot_area_all_input == 2:
            print("""
            Bot Lift Components Parts List:
                """)
            print(pdtabulate_bot(bot_lift_main))
        if bot_area_all_input == 3:
            print(main_back())
