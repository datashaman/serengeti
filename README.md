# serengeti

[![PyPI - Version](https://img.shields.io/pypi/v/serengeti.svg)](https://pypi.org/project/serengeti)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/serengeti.svg)](https://pypi.org/project/serengeti)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
git clone https://github.com/datashaman/serengeti.git
cd serengeti
pip install hatch
hatch run python -m serengeti.app
```

## Sample output

```
❯ hatch run python -m serengeti.app
Hardware accelerator e.g. GPU is available in the environment, but no `device` argument is passed to the `Pipeline` object. Model will be on CPU.
[{'score': 0.07973083108663559,
  'sequence': 'ẹ jọwọ, ẹ ọmọ mi',
  'token': 8418,
  'token_str': 'ọmọ'},
 {'score': 0.049467019736766815,
  'sequence': 'ẹ jọwọ, ẹ fẹ́ràn mi',
  'token': 156595,
  'token_str': 'fẹ́ràn'},
 {'score': 0.03016754984855652,
  'sequence': 'ẹ jọwọ, ẹ gbàgbé mi',
  'token': 204050,
  'token_str': 'gbàgbé'},
 {'score': 0.02831439860165119,
  'sequence': 'ẹ jọwọ, ẹ kọ mi',
  'token': 10730,
  'token_str': 'kọ'},
 {'score': 0.02368140034377575,
  'sequence': 'ẹ jọwọ, ẹ bẹ̀rù mi',
  'token': 115382,
  'token_str': 'bẹ̀rù'}]
```

## License

`serengeti` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
