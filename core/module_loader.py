import importlib
import os


def load_module(app, module_dir, func, named=False, pattern=None, filters=False):

    command_modules = filter(
        lambda filename: filename.endswith(".py") and filename != "__init__.py",
        os.listdir(module_dir)
    )

    for command_module in command_modules:
        command_name = command_module[:-3]
        module = importlib.import_module(f"{module_dir}.{command_name}")

        try:
            handler_func = module.handler
            handler_filters = filters and module.handler_filters
            print(f"✅️ {module_dir}: \"{command_name}\" импортирован.")
        except AttributeError:
            print(f"⚠️ {module_dir}: В модуле {command_module} нет 'handler'. Пропускаем.")
            continue

        args = []
        if named:
            app.add_handler(func(command_name, handler_func))
        elif pattern:
            app.add_handler(func(handler_func, pattern=f"^{command_name}:"))
        elif filters:
            app.add_handler(func(handler_filters, handler_func))
        else:
            app.add_handler(func(handler_func))
