def dailytemp(temperature):
    result=[0]*len(temperature)
    stack=[]
    for i,temp in enumerate(temperature):
        while stack and temp>temperature[stack[-1]]:
            prev_index=stack.pop()
            result[prev_index]=i-prev_index
        stack.append(i)
    return result

# Merge
merged_df = pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)

