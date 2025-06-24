<!-- Stylish GitHub README HTML (Markdown-compatible) -->

<h2>🚀 <u>Requirements</u></h2>

<p>
  <img src="https://img.shields.io/badge/Python-Installed-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-Running-brightgreen?logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/mysql--connector--python-Installed-yellow?logo=pypi" />
</p>

<ul>
  <li>✅ Make sure <strong>Python</strong> is installed: <code>python --version</code></li>
  <li>✅ Ensure <strong>MySQL Server</strong> is installed and running</li>
  <li>✅ Install the connector with:
    <pre><code>pip install mysql-connector-python</code></pre>
  </li>
</ul>

<hr style="border: 1px solid #ccc; margin: 20px 0;">

<h2>🛠️ <u>MySQL Setup</u></h2>

<p><strong>📌 Run the following commands inside your MySQL terminal:</strong></p>

<pre><code style="background-color:#f4f4f4">
CREATE DATABASE testdb;
USE testdb;
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
</code></pre>
