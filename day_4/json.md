### What Does JSON Stand For?
- **JSON** stands for **JavaScript Object Notation**.

### What Is JSON Used For?
- JSON is used to **store and exchange data** between a server and a client. It is primarily used in web applications for data interchange, such as in APIs.
- It is lightweight, easy to read, and commonly used for sending data between systems.

### What Is JSON Written In?
- JSON is a **text format** that is completely language-independent but uses conventions familiar to programmers of the **JavaScript** language.

### Simple Example of JSON:
```json
{
    "name": "John",
    "age": 30,
    "is_employee": true,
    "skills": ["Python", "JavaScript"],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
```
### Serialization vs encoding
| Aspect                  | Encoding                                                                                               | Serializing                                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Definition**          | Converting data into a specific format (usually bytes or text) suitable for transmission or storage.   | Converting complex data structures into a storable or transmittable format that can be reconstructed later. |
| **Purpose**             | To ensure data can be properly transmitted or stored across different systems using a standard format. | To persist or transmit complex data structures and reconstruct them in their original form later.           |
| **Use Cases**           | Character encoding (UTF-8, ASCII), URL encoding, Base64 encoding.                                      | Saving objects to files, sending data over a network, inter-process communication.                          |
| **Input Data**          | Typically text or binary data that needs to be converted into a specific format.                       | Complex data structures like objects, dictionaries, lists, etc.                                             |
| **Output Format**       | Encoded text or bytes (e.g., UTF-8 encoded bytes, Base64 strings).                                     | Serialized data in formats like JSON strings, XML documents, or binary data (e.g., Pickle files).           |
| **Reversibility**       | Reversible through decoding using the same encoding scheme.                                            | Reversible through deserialization, reconstructing the original data structure.                             |
| **Language Dependency** | Generally language-agnostic, especially for standard encodings like UTF-8.                             | Can be language-specific (e.g., Pickle in Python) or language-agnostic (e.g., JSON, XML).                   |

Serializing is about converting complex data structures into a format that can be stored or transmitted and then reconstructed later. It's used for persisting objects or data structures and often involves more complex data types than simple strings or bytes.

