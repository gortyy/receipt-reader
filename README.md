## Usage

```python
from receipt_reader import Parser, Reader

receipt_reader = Reader("tests/resource/receipt.png")
receipt_contents = receipt_reader.read()
receipt_parsers = Parser(receipt_contents)
```
