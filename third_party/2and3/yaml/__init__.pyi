from typing import Optional, Any, Iterator, Sequence, Union, IO
from yaml.error import *  # noqa: F403
from yaml.tokens import *  # noqa: F403
from yaml.events import *  # noqa: F403
from yaml.nodes import *  # noqa: F403
from yaml.loader import *  # noqa: F403
from yaml.dumper import *  # noqa: F403
from . import resolver  # Help mypy a bit; this is implied by loader and dumper
from .cyaml import *

__with_libyaml__: Any
__version__: str

def scan(stream, Loader=...): ...
def parse(stream, Loader=...): ...
def compose(stream, Loader=...): ...
def compose_all(stream, Loader=...): ...
def load(stream: Union[str, IO[str]], Loader=...) -> Any: ...
def load_all(stream: Union[str, IO[str]], Loader=...) -> Iterator[Any]: ...
def full_load(stream: Union[str, IO[str]]) -> Any: ...
def full_load_all(stream: Union[str, IO[str]]) -> Iterator[Any]: ...
def safe_load(stream: Union[str, IO[str]]) -> Any: ...
def safe_load_all(stream: Union[str, IO[str]]) -> Iterator[Any]: ...
def emit(events, stream=..., Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=...): ...
def serialize_all(nodes, stream=..., Dumper=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...): ...
def serialize(node, stream=..., Dumper=..., **kwds): ...
def dump_all(documents: Sequence[Any], stream: IO[str] = ..., Dumper=..., default_style=..., default_flow_style=..., canonical=..., indent=..., width=..., allow_unicode=..., line_break=..., encoding=..., explicit_start=..., explicit_end=..., version=..., tags=...) -> Any: ...
def dump(data: Any, stream: Optional[IO[str]] = ..., Dumper=..., **kwds) -> Any: ...
def safe_dump_all(documents: Sequence[Any], stream: IO[str] = ..., **kwds) -> Any: ...
def safe_dump(data: Any, stream: IO[str] = ..., **kwds) -> Any: ...
def add_implicit_resolver(tag, regexp, first=..., Loader=..., Dumper=...): ...
def add_path_resolver(tag, path, kind=..., Loader=..., Dumper=...): ...
def add_constructor(tag, constructor, Loader=...): ...
def add_multi_constructor(tag_prefix, multi_constructor, Loader=...): ...
def add_representer(data_type, representer, Dumper=...): ...
def add_multi_representer(data_type, multi_representer, Dumper=...): ...

class YAMLObjectMetaclass(type):
    def __init__(self, name, bases, kwds) -> None: ...

class YAMLObject(metaclass=YAMLObjectMetaclass):
    yaml_loader: Any
    yaml_dumper: Any
    yaml_tag: Any
    yaml_flow_style: Any
    @classmethod
    def from_yaml(cls, loader, node): ...
    @classmethod
    def to_yaml(cls, dumper, data): ...
