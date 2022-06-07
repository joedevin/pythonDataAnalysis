import pandas as pd

df21 = pd.read_csv("archive/LCA_FY_2021.csv", usecols=["Visa_Class", "SOC_Title", "Case_Status"])

#Overview Visa Information and total
print("2021 Tempory Work Visa Overview Information")
print(df21["Visa_Class"].value_counts()) #counts the kinds of visas included in the list
print() #space
sum = df21["Visa_Class"].count() + 0 #sum of all visas together
print(f"Total Tempory Work Visas: {sum}")
print() #space
print() #space

#status overview information and totals
print(df21["Case_Status"].value_counts())
print()#space
print()#space

#reread data to exclude the visa classg
df21 = pd.read_csv("archive/LCA_FY_2021.csv", usecols=["SOC_Title", "Case_Status"])

#Information of Software related work
df21_SOCTitle_mask = df21["SOC_Title"].str.contains("Software")
df21_CaseStatus_cert_mask = df21["Case_Status"] == "Certified"
df21_CaseStatus_denied_mask = df21["Case_Status"] == "Denied"
print(df21[df21_SOCTitle_mask & df21_CaseStatus_cert_mask].value_counts())
software_total = df21[df21_SOCTitle_mask & df21_CaseStatus_cert_mask].count()
print()#space
print(df21[df21_SOCTitle_mask & df21_CaseStatus_denied_mask].value_counts())
software_denied_total = df21[df21_SOCTitle_mask & df21_CaseStatus_denied_mask].count()

print(f"Total Software Approved: {software_total}")
print(f"Total Software Denied: {software_denied_total}")
print()#space
print()#space

#filter computer & certified or denied
df21_SOCTitle_mask2 = df21["SOC_Title"].str.contains("Computer")
df21_CaseStatus_mask = df21["Case_Status"] == "Certified"
df21_CaseStatus_denied_mask = df21["Case_Status"] == "Denied"
print(df21[df21_SOCTitle_mask2 & df21_CaseStatus_mask].value_counts())
computer_total = df21[df21_SOCTitle_mask2 & df21_CaseStatus_mask].count()
print()#space
print(df21[df21_SOCTitle_mask2 & df21_CaseStatus_denied_mask].value_counts())
computer_denied_total = df21[df21_SOCTitle_mask2 & df21_CaseStatus_denied_mask].count()
print(f"Total Computer Area Approved: {computer_total}")
print(f"Total Computer Area Denied: {computer_denied_total}")
print()#space
print()#space


#filter medical & certified or denied
df21_SOCTitle_mask3 = df21["SOC_Title"].str.contains("Medical")
df21_CaseStatus_mask = df21["Case_Status"] == "Certified"
df21_CaseStatus_denied_mask = df21["Case_Status"] == "Denied"
print(df21[df21_SOCTitle_mask3 & df21_CaseStatus_mask].value_counts())
medical_total = df21[df21_SOCTitle_mask3 & df21_CaseStatus_mask].count()
print()#space
print(df21[df21_SOCTitle_mask3 & df21_CaseStatus_denied_mask].value_counts())
medical_denied_total = df21[df21_SOCTitle_mask3 & df21_CaseStatus_denied_mask].count()
print(f"Total Medical Area Approved: {medical_total}")
print(f"Total Medical Area Denied: {medical_denied_total}")
print()#space
print()#space

input("prompt: ")
