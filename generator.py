import ast

module = ast.Module(
    body=[
        ast.Assign(
            targets=[ast.Name(id="x", ctx=ast.Store())],
            value=ast.Constant(value=1),
            lineno=2,
        )
    ],
    type_ignores=[],
)

module = ast.Module(
    body=[
        ast.ClassDef(
            name="LoginApp",
            bases=[],
            keywords=[],
            body=[
                ast.FunctionDef(
                    name="__init__",
                    lineno=1,
                    args=ast.arguments(
                        posonlyargs=[],
                        args=[
                            ast.arg(arg="self"),
                            ast.arg(
                                arg="repo",
                                annotation=ast.Name(
                                    id="LoginRepositoryInterface", ctx=ast.Load()
                                ),
                            ),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        ast.Assign(
                            lineno=1,
                            targets=[
                                ast.Attribute(
                                    value=ast.Name(id="self", ctx=ast.Load()),
                                    attr="repo",
                                    ctx=ast.Store(),
                                )
                            ],
                            value=ast.Name(id="repo", ctx=ast.Load()),
                        )
                    ],
                    decorator_list=[ast.Name(id="inject", ctx=ast.Load())],
                ),
                ast.FunctionDef(
                    name="login",
                    lineno=1,
                    args=ast.arguments(
                        posonlyargs=[],
                        args=[
                            ast.arg(arg="self"),
                            ast.arg(
                                arg="username",
                                annotation=ast.Name(id="str", ctx=ast.Load()),
                            ),
                            ast.arg(
                                arg="password",
                                annotation=ast.Name(id="str", ctx=ast.Load()),
                            ),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        ast.Return(
                            value=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Call(
                                        func=ast.Name(id="LoginCruds", ctx=ast.Load()),
                                        args=[
                                            ast.Attribute(
                                                value=ast.Name(
                                                    id="self", ctx=ast.Load()
                                                ),
                                                attr="repo",
                                                ctx=ast.Load(),
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                    attr="login",
                                    ctx=ast.Load(),
                                ),
                                args=[
                                    ast.Name(id="username", ctx=ast.Load()),
                                    ast.Name(id="password", ctx=ast.Load()),
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        )
    ],
    type_ignores=[],
)

print(ast.unparse(module))

