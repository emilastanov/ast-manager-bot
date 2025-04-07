import importlib
import os


def load_module(app, module_dir, func, named=False, pattern=None):

    command_modules = filter(
        lambda filename: filename.endswith(".py") and filename != "__init__.py",
        os.listdir(module_dir)
    )

    for command_module in command_modules:
        command_name = command_module[:-3]
        module = importlib.import_module(f"{module_dir}.{command_name}")

        try:
            handler_func = module.handler
            print(f"✅️ {module_dir}: \"{command_name}\" импортирован.")
        except AttributeError:
            print(f"⚠️ {module_dir}: В модуле {command_module} нет 'handler'. Пропускаем.")
            continue

        if named:
            app.add_handler(func(command_name, handler_func))
        elif pattern:
            app.add_handler(func(handler_func, pattern=f"^{command_name}:"))
        else:
            app.add_handler(func(handler_func))
