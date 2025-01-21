# FLAMES Game Web Application

✨ A fun and nostalgic web app to determine relationship compatibility based on the classic 90's FLAMES game! Built using Python and Streamlit, this app recreates the joy of discovering connections with your friends, family, or special someone.

---

## Features

- **User-Friendly Interface**: Enter two names and let the app do the magic!
- **FLAMES Algorithm**: Implements the traditional FLAMES logic to compute relationships.
- **Fun Results**: Outputs relationships like Friends, Lovers, Affectionate, Marriage, Enemies, or Siblings.
- **Interactive Experience**: Built using Streamlit for a seamless and engaging user experience.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd flames-game
   ```

3. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open the provided local URL in your browser to start playing!

---

## Code Overview

The FLAMES logic involves:
- **Removing common characters**: Simplifies the names to find the total remaining characters.
- **Mapping to the FLAMES acronym**: Determines the relationship based on the remaining character count.

The main functions in the code include:

1. `remove_common_chars(name1, name2)`: Computes the total number of characters left after removing common letters from the two names.
2. `flames_result(remaining_chars)`: Determines the FLAMES relationship using the character count.
3. `flames_relationship(name1, name2)`: Integrates the above functions and maps the result to a descriptive relationship type.

---

## Example

**Input:**
- Name 1: Alice
- Name 2: Bob

**Output:**
The relationship between **Alice** and **Bob** is: **Lovers** 💖

---

## Author

**Vishnuprasaath M**
- LinkedIn: [Vishnuprasaath M](https://www.linkedin.com/in/vishnuprasaath-m-0298a0287)

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

```
MIT License

Copyright (c) 2025 Vishnuprasaath M

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

---

🎉 Enjoy playing and sharing this nostalgic game with your friends!