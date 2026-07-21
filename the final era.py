student_data={"id1":{"name":"Sara","class":5,"subject":"english,Maths,Science"},
            "id2":{"name":"sathvik","class":5,"subject":"english,Maths,Science"},
            "id3":{"name":"Sara","class":5,"subject":"english,Maths,Science"},
             "id4":{"name":"david","class":5,"subject":"english,Maths,Science"}}
print(student_data)
result={}
seen_keys=[]
for student_id, details in student_data.items():
    unique_keys=(details["name"],details["class"],details["subject"])
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id]=details
print(result)

              
