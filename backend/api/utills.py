def format_list(data):
    """
    Formatting data for the frontend tree view
    :param data: list of tasks from database
    :return: list of formatted tasks
    """
    tasks = {task['id']: {'key': str(task['id']), 'label': task['name'], 'children': []} for task in data}
    parented = []
    for task in data:
        if task['parent_task']:
            tasks[task['parent_task']]['children'].append(tasks[task['id']])
            parented.append(str(task['id']))
    return [task for task in tasks.values() if task["key"] not in parented]
