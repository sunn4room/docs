# Markdown Demo

## 图片

![plantuml](http://www.plantuml.com/plantuml/png/LO-zgiCm38LtFONGT6yXGnlwCuMyGOTs2nr4AzE0aq2il7-je0PtCkZxZdJS9kLPbo72t-uVgwh1FY3Tfa7mBaa9zIqZ01hgT5xaWSHFxQSHzsHpqzr2p5gpyPgG4tATvnAJ65xjQvPdr6sx0Kj62Lh4ZvI1HzqewCdf-Ee3V5zOPR0MNU2OYh870d29w-sVaPEMJNvld0dyUZ6yaEzfyxCCyGC0)

```plantuml
Bob->Alice
```

```{plantweb}plantuml
Bob->Alice
```

```{uml}plantuml
Bob->Alice
```

```{uml}
Bob->Alice
```

```{uml}
---
alt: This is a nice UML diagram. Indeed.
align: left
target: #options
---
actor Foo1
boundary Foo2
control Foo3
entity Foo4
database Foo5
Foo1 -> Foo2 : To boundary
Foo1 -> Foo3 : To control
Foo1 -> Foo4 : To entity
Foo1 -> Foo5 : To database
```
