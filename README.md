# WHOIS Information

This Python script retrieves and displays WHOIS information for a given domain.

## Requirements

- Python 3.x
- `whois` command-line tool

## Usage

```bash
python whois.py <domain>
```

### Example

```bash
python whois.py example.com
```

## Output

The script will print key WHOIS details, such as:

- Domain Registrar
- Registration Date
- Expiration Date
- Registrant Name
- Name Servers

## Notes

- Ensure the `whois` tool is installed on your system.
- Works on Unix-based systems (Linux, macOS).
