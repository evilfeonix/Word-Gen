# WordList Generator - `WORD-GEN`

### Version: 1.0  
### Author: EvilFeonix  
### Date: 16 - DECEMBER - 2024  
### Website: [www.evilfeonix.com](http://www.evilfeonix.com)  
### Email: evilfeonix@gmail.com  

---

## Description
`WORD-GEN` is a Python-based tool designed for generating custom wordlists. By combining words from an input list, the tool creates permutations and combinations to generate a comprehensive list of passwords or keywords. 

This tool is ideal for security professionals and ethical hackers to use in penetration testing scenarios or other legal activities.

**⚠ Disclaimer**:  
The creators of this tool are not responsible for any misuse or damage caused by its usage. Always use this tool responsibly and for ethical purposes only.

---

## Features
- Generates custom wordlists using permutations and combinations of provided words.
- Allows control over the minimum and maximum password lengths.
- Automatically saves generated wordlists in a timestamped file within a structured directory.
- Includes error handling for missing or invalid files.
- Provides an intuitive, colorful command-line interface.

---

## Installation
    Clone the repository:
   ```bash
   git clone https://github.com/evilfeonix/wordlist-generator.git
   cd wordlist-generator
  ```

---
  
## Usage
    Basic Command:
  ```bash
python3 wordlist_generator.py [OPTIONS...]
  ```

---

## Options

| **Option**    | **Description**                                            | **Default**       |
|---------------|------------------------------------------------------------|-------------------|
| `--iniList`   | Path to the input file containing initial words.           | `config.ini`      |
| `--minLen`    | Minimum length of generated passwords.                     | `4`               |
| `--maxLen`    | Maximum length of generated passwords.                     | `14`              |

---

## Examples:
    Generate a wordlist:

  ```bash 
python3 wordlist_generator.py --iniList words.txt --minLen 6 --maxLen 12
  ```

---

## Use default parameters:

  ```bash
python3 wordlist_generator.py
  ```

---

## Output
    The generated wordlist is saved in the WordLists directory.
    Files are named using the current date and time for easy identification:
  ```bash
WordLists/wordlist_2024-12-16_12-00-00.txt
  ```

---

## Screenshots
Tool Banner:

---

## Contributing

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.

---

## Disclaimer

**Educational Purpose Only:**

This tool is intended to help ethical hackers and cybersecurity professionals generate custom wordlists for legal use. Misusing this tool for unauthorized activities is against the law.


**Responsibility:**

The developers are not responsible for any misuse or damage caused by this tool. Use it responsibly.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Wordlist Generating! 🚀
