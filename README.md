# Pydantic name resolution bug report

Under certain conditions, pydantic v2 will fail to resolve a type reference:

```
pydantic.errors.PydanticUndefinedAnnotation: name 'LegalEntity' is not defined

For further information visit https://errors.pydantic.dev/2.10/u/undefined-annotation
```

But in pydantic v1, the same code works as-is.

Relevant code is in `src/pydantic_bug_repro/`.

## Reproducing

With `uv` installed:

**should pass**
```
uv run --extra=pv1 python -c 'import pydantic_bug_repro'
```

**should fail**
```
uv run --extra=pv2 python -c 'import pydantic_bug_repro'
```


<details>
<summary>Full stack trace</summary>


```
Traceback (most recent call last):
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1225, in _common_field_schema
    evaluated_type = _typing_extra.eval_type(field_info.annotation, *self._types_namespace)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_typing_extra.py", line 577, in eval_type
    return eval_type_backport(value, globalns, localns)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_typing_extra.py", line 609, in eval_type_backport
    return _eval_type_backport(value, globalns, localns, type_params)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_typing_extra.py", line 633, in _eval_type_backport
    return _eval_type(value, globalns, localns, type_params)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_typing_extra.py", line 667, in _eval_type
    return typing._eval_type(  # type: ignore
  File "/Users/robert/.local/share/uv/python/cpython-3.9.18-macos-aarch64-none/lib/python3.9/typing.py", line 292, in _eval_type
    return t._evaluate(globalns, localns, recursive_guard)
  File "/Users/robert/.local/share/uv/python/cpython-3.9.18-macos-aarch64-none/lib/python3.9/typing.py", line 554, in _evaluate
    eval(self.__forward_code__, globalns, localns),
  File "<string>", line 1, in <module>
NameError: name 'LegalEntity' is not defined

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "pydantic-bug-repro/src/pydantic_bug_repro/__init__.py", line 3, in <module>
    from .worker import Worker as Worker
  File "pydantic-bug-repro/src/pydantic_bug_repro/worker.py", line 18, in <module>
    from .compensation import Compensation
  File "pydantic-bug-repro/src/pydantic_bug_repro/compensation.py", line 16, in <module>
    Compensation.model_rebuild()
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/main.py", line 594, in model_rebuild
    return _model_construction.complete_model_class(
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_model_construction.py", line 602, in complete_model_class
    schema = cls.__get_pydantic_core_schema__(cls, handler)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/main.py", line 702, in __get_pydantic_core_schema__
    return handler(source)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_schema_generation_shared.py", line 84, in __call__
    schema = self._handler(source_type)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 610, in generate_schema
    schema = self._generate_schema_inner(obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 879, in _generate_schema_inner
    return self._model_schema(obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 691, in _model_schema
    {k: self._generate_md_field_schema(k, v, decorators) for k, v in fields.items()},
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 691, in <dictcomp>
    {k: self._generate_md_field_schema(k, v, decorators) for k, v in fields.items()},
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1071, in _generate_md_field_schema
    common_field = self._common_field_schema(name, field_info, decorators)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1263, in _common_field_schema
    schema = self._apply_annotations(
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 2056, in _apply_annotations
    schema = get_inner_schema(source_type)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_schema_generation_shared.py", line 84, in __call__
    schema = self._handler(source_type)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 2037, in inner_handler
    schema = self._generate_schema_inner(obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 884, in _generate_schema_inner
    return self.match_type(obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 986, in match_type
    return self._match_generic_type(obj, origin)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1014, in _match_generic_type
    return self._union_schema(obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1325, in _union_schema
    choices.append(self.generate_schema(arg))
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 605, in generate_schema
    from_property = self._generate_schema_from_property(obj, obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 759, in _generate_schema_from_property
    schema = get_schema(
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/main.py", line 702, in __get_pydantic_core_schema__
    return handler(source)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_schema_generation_shared.py", line 84, in __call__
    schema = self._handler(source_type)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 879, in _generate_schema_inner
    return self._model_schema(obj)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 691, in _model_schema
    {k: self._generate_md_field_schema(k, v, decorators) for k, v in fields.items()},
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 691, in <dictcomp>
    {k: self._generate_md_field_schema(k, v, decorators) for k, v in fields.items()},
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1071, in _generate_md_field_schema
    common_field = self._common_field_schema(name, field_info, decorators)
  File "pydantic-bug-repro/.venv/lib/python3.9/site-packages/pydantic/_internal/_generate_schema.py", line 1227, in _common_field_schema
    raise PydanticUndefinedAnnotation.from_name_error(e) from e
pydantic.errors.PydanticUndefinedAnnotation: name 'LegalEntity' is not defined

For further information visit https://errors.pydantic.dev/2.10/u/undefined-annotation
```

</details>
