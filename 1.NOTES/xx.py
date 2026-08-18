
1.ATTRIBUTES OF THE HTML >> 

<!
1️⃣ Structure tags
<html>, <head>, <body>

2️⃣ Text formatting tags
<p>, <h1>–<h6>, <b>, <i>, <em>, <strong>

3️⃣ List tags
<ul>, <ol>, <li>

4️⃣ Table tags
<table>, <tr>, <td>, <th>

5️⃣ Form tags
<form>, <input>, <textarea>, <button>

6️⃣ Media tags
<img>, <audio>, <video>

7️⃣ Semantic tags (HTML5)
<header>, <footer>, <section>, <article>, <nav>
>



2. HTML STYLES >> 

The HTML style attribute is used to add styles to an element, such as color, font, size, and more.
* in the html the style can be defined as total 3 types INLINE STYLE , INTERNAL STYLE , EXTERNAL STYLE  . 
*
The properties are SAME in Inline, Internal, and External CSS.
Only the location changes, not the properties.

✅ Common CSS Properties (Simple List)
🎨 1️⃣ Text Properties

color → Text color

font-size → Size of text

font-family → Style of font

font-weight → Bold text

text-align → Left, right, center

text-decoration → underline, none

text-transform → uppercase, lowercase

🎨 2️⃣ Background Properties

background-color → Background color

background-image → Set image

background-size → Size of image

📦 3️⃣ Box Properties

margin → Space outside element

padding → Space inside element

border → Border around element

width → Width of element

height → Height of element

📍 4️⃣ Positioning Properties

display → block, inline, none

position → relative, absolute

top, left, right, bottom



#diff form writing a text(a part of styles)
<b> - Bold text
<strong> - Important text
<i> - Italic text
<em> - Emphasized text
<mark> - Marked text
<small> - Smaller text
<del> - Deleted text
<ins> - Inserted text
<sub> - Subscript text
<sup> - Superscript text


#3.
✅ What is a Form in HTML?

👉 A form is used to collect user input.
👉 Example: name, email, password, feedback, etc.
👉 Data is sent to a server.

✅ Basic Structure of Form
<form action="file_name">
    form elements
</form>

<form> → Starting of form

</form> → End of form

action → Where data will go after submit

✅ Now Understand Your Code
<form action="/action_page.php">

👉 action="/action_page.php"
Means: When user clicks Submit, data goes to action_page.php.

1️⃣ Label Tag
<label for="fname">First name:</label>

👉 <label> gives name to input field
👉 for="fname" connects label with input id="fname"

2️⃣ Input Tag
<input type="text" id="fname" name="fname" value="John">
Important Attributes:

type="text" → Text box

id="fname" → Unique identity

name="fname" → Name used to send data to server

value="John" → Default value inside box

3️⃣ Line Break
<br>

👉 Moves content to next line

4️⃣ Submit Button
<input type="submit" value="Submit">

👉 type="submit" → Creates submit button
👉 value="Submit" → Text written on button

✅ Important Input Types

text

password

email

number

radio

checkbox

submit

file

date

Example:

<input type="password">
<input type="email">
<input type="radio">
✅ Simple Definition for Exam

ptr.
#input types = "SYNTAX" , name="IT WILL HELP TO TRANSFER THE DATA" , values = "IT WILL GIVE NAME TO THE BUTTONS ."
#action="data.php" → Data goes to this file



#4.

#5.HTML TABLES >> 

Alfreds Futterkiste              Maria Anders         Germany
Centro comercial Moctezuma       Francisco Chang      Mexico
Ernst Handel                     Roland Mendel        Austria
Island Trading                   Helen Bennett        UK
Laughing Bacchus Winecellars     Yoshi Tannamuri      Canada
Magazzini Alimentari Riuniti     Giovanni Rovelli     Italy


* A table in HTML consists of table cells inside rows and columns.
<table> - - </table>
<tr> -- </tr>
<td> -- </td>




















































