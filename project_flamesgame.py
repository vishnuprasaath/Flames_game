import streamlit as st

#FLAMES Game Logic
def remove_common_chars(name1, name2):
    list1 = list(name1)
    list2 = list(name2)

    for char in list1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)
    
    remaining_chars = len(list1) + len(list2)
    return remaining_chars

def flames_result(remaining_chars):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames) > 1:
        split_index = (remaining_chars % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

def flames_relationship(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    remaining_chars = remove_common_chars(name1, name2)
    result = flames_result(remaining_chars)

    relationship_dict = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }

    return relationship_dict[result]


st.title("✨ 90's Popular FLAMES Game ✨")
st.subheader("Find out your relationship compatibility in a fun way!")

# Input Section
st.write("Enter the names of two people to uncover their relationship type based on the FLAMES game.")
name1 = st.text_input("Enter the first name:", placeholder="Type a name (e.g., Alice)")
name2 = st.text_input("Enter the second name:", placeholder="Type another name (e.g., Bob)")

if st.button("Find Relationship"):
    if name1.strip() and name2.strip():
        relationship = flames_relationship(name1, name2)
        st.success(f"The relationship between **{name1}** and **{name2}** is: **{relationship}** 💖")
    else:
        st.error("Please enter both names to play the game.")

# Footer
st.write("---")
st.write("🎉 Have fun playing this nostalgic game and share it with your friends! 🎉")
