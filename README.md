# Task Manager CLI

A Python-based **command-line task management system** with **AI-powered natural language processing**. Features intelligent task extraction, multi-provider AI support, advanced filtering, and comprehensive task tracking with persistent JSON storage.

---

## Features

- **AI-Powered Task Creation**: Create tasks using natural language with support for Claude, ChatGPT, and Grok
- **Multi-Provider Support**: Seamlessly switch between Anthropic, OpenAI, and xAI providers
- **Smart Task Extraction**: AI automatically extracts title, description, priority, and status from plain text
- **Advanced Filtering**: Filter tasks by status (Pending, In Progress, Completed) or priority (High, Medium, Low)
- **Keyword Search**: Find tasks quickly by searching titles and descriptions (case-insensitive)
- **Statistics Dashboard**: Real-time overview of task distribution and completion rates
- **Sequential IDs**: Human-friendly task identifiers (1, 2, 3...) for easy reference
- **Persistent Storage**: Automatic JSON-based save with data integrity
- **Input Validation**: Enum-based validation prevents invalid task data
- **Formatted Output**: Professional table displays using `tabulate`
- **Settings Menu**: Easy configuration management for storage paths and AI providers

---

## Requirements

- Python 3.8+
- Required libraries:
  - `tabulate`
  - `anthropic`
  - `openai`

```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   pip install tabulate anthropic openai
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

### First Run - Automatic Setup

```bash
python main.py
```

On first run, the application automatically creates a default `config.json`:

```
=== TASK MANAGER ===
1. Add task
2. View all tasks
3. Delete task
4. Mark complete
5. Filter by status
6. Filter by priority
7. Search
8. Statistics
9. Settings
0. Exit

Enter choice:
```

**Default Configuration:**
- **Storage**: `./tasks.json` (created automatically)
- **AI Features**: Disabled (can be enabled via Settings)

### Enabling AI Features

Navigate to Settings (option 9) to configure AI:

```
Enter choice: 9

=== TASK MANAGER SETTINGS ===
1. Update storage path
2. Enable/Update AI
0. Exit settings

Select an option: 2

Enter the AI model provider (Anthropic, xAI, OpenAI):
anthropic

Enter the desired AI model (e.g. gpt-3.5-turbo, grok-beta, claude-sonnet-4-20250514):
claude-sonnet-4-20250514

Enter the API key for your chosen provider:
sk-ant-xxxxxxxxxxxxx

Config updated
```

### Creating Tasks with AI

Once AI is enabled, you can create tasks using natural language:

```
Enter choice: 1
Use AI to create task from description? (y/n): y

Describe your task in natural language:
high priority: finish the project report by Friday

AI extracted:
Title: Finish the project report
Description: Complete by Friday
Priority: High
Status: Pending

Create this task? (y/n): y
Task created with AI!
```

### Creating Tasks Manually

```
Enter choice: 1
Use AI to create task from description? (y/n): n

Please enter the title:
Review pull requests

Please enter any additional information/description:
Check code quality and provide feedback

Please enter the priority (['High', 'Medium', 'Low']):
Medium

Please enter the status (['Pending', 'In Progress', 'Completed']):
Pending

New task created
```

---

## File Structure

```
task-manager-cli/
├── main.py              # CLI interface and menu system
├── task_manager.py      # Core business logic
├── task.py              # Task class with enums
├── storage.py           # JSON persistence layer
├── utils.py             # Helper functions
├── config.py            # Configuration management
├── ai/
│   ├── ai_helper.py     # AI extraction logic
│   ├── claude.py        # Anthropic client
│   ├── gpt.py           # OpenAI client
│   └── grok.py          # xAI client
├── tasks.json           # Task database (auto-created)
├── config.json          # Configuration (auto-created)
├── config.example.json  # Example configuration
├── requirements.txt     # Dependencies
└── README.md
```

### Example `config.json`

```json
{
  "main": {
    "storage": "./tasks.json"
  },
  "ai": {
    "enabled": true,
    "provider": "anthropic",
    "model": "claude-sonnet-4-20250514",
    "api_key": "sk-ant-xxxxxxxxxxxxx"
  }
}
```

### Example `tasks.json`

```json
[
  {
    "id": 1,
    "title": "Finish project report",
    "desc": "Complete by Friday",
    "priority": "High",
    "status": "Pending",
    "creation_date": "2026-02-14T14:30:00.123456"
  },
  {
    "id": 2,
    "title": "Review pull requests",
    "desc": "Check code quality",
    "priority": "Medium",
    "status": "In Progress",
    "creation_date": "2026-02-14T15:45:00.654321"
  }
]
```

### Example Output

**View All Tasks:**
```
ID  Title                          Description           Priority  Status
--  -----------------------------  --------------------  --------  -----------
1   Finish project report          Complete by Friday    High      Pending
2   Review pull requests           Check code quality    Medium    In Progress
3   Buy groceries                  Milk, bread, eggs     Low       Completed
```

**Statistics:**
```
=== STATISTICS ===
Total tasks: 12
Completed: 5
In Progress: 4
Pending: 3
```

---

## AI Provider Configuration

### Supported Providers

| Provider | Model Examples | API Key Format |
|----------|----------------|----------------|
| **Anthropic** | claude-opus-4-20250514<br>claude-sonnet-4-20250514<br>claude-haiku-4-20250514 | sk-ant-... |
| **OpenAI** | gpt-4<br>gpt-4-turbo<br>gpt-3.5-turbo | sk-... |
| **xAI** | grok-beta<br>grok-2-latest<br>grok-vision-beta | xai-... |

### Provider Selection

The application automatically uses the correct API endpoint based on the configured provider:

- **Anthropic**: Direct Anthropic API (`https://api.anthropic.com`)
- **OpenAI**: Standard OpenAI API (`https://api.openai.com`)
- **xAI**: OpenAI-compatible API (`https://api.x.ai/v1`)

### AI Extraction Examples

**Input:** `"high priority: finish report by Friday"`
**Output:**
```json
{
  "title": "Finish report",
  "desc": "Complete by Friday",
  "priority": "High",
  "status": "Pending"
}
```

**Input:** `"buy milk"`
**Output:**
```json
{
  "title": "Buy milk",
  "desc": "",
  "priority": "Medium",
  "status": "Pending"
}
```

**Input:** `"schedule meeting about Q1 planning"`
**Output:**
```json
{
  "title": "Schedule meeting about Q1 planning",
  "desc": "",
  "priority": "Medium",
  "status": "Pending"
}
```

---

## Task Operations

### Adding Tasks
- **With AI**: Natural language input with confirmation
- **Manual**: Step-by-step prompts with validation
- **Automatic Save**: Tasks persist immediately

### Viewing Tasks
- **View All**: Display complete task list in table format
- **Filter by Status**: Show only Pending, In Progress, or Completed tasks
- **Filter by Priority**: Show only High, Medium, or Low priority tasks
- **Search**: Find tasks by keyword in title or description

### Modifying Tasks
- **Mark Complete**: Change task status to Completed by ID
- **Delete**: Remove tasks by ID with confirmation

### Statistics
- **Total Tasks**: Count of all tasks
- **By Status**: Breakdown of Pending, In Progress, Completed
- **Quick Overview**: At-a-glance productivity metrics

---

## Priority Levels

- **High**: Urgent or critical tasks requiring immediate attention
- **Medium**: Important tasks without immediate deadlines (default for AI extraction)
- **Low**: Nice-to-have or long-term tasks

---

## Status Types

- **Pending**: Not yet started (default for new tasks)
- **In Progress**: Currently being worked on
- **Completed**: Finished tasks

---

## Error Handling

The application handles common issues gracefully:

- **Missing configuration**: Automatically creates default config
- **Invalid task IDs**: Clear error messages with guidance
- **AI extraction failures**: Automatic fallback to manual entry
- **Invalid input**: Re-prompts until valid data provided
- **API errors**: Informative error messages with retry options
- **Network issues**: Graceful degradation to manual mode

---

## Use Cases

- **Personal Productivity**: Track daily tasks and goals
- **Project Management**: Organize work items by priority
- **Study Planning**: Manage assignments and deadlines
- **Quick Capture**: Use AI for rapid task entry without interrupting workflow
- **Team Coordination**: Share task lists via version control
- **Workflow Tracking**: Monitor task status progression

---

## Notes

- **Task IDs** are sequential integers (1, 2, 3...) and do not reuse deleted IDs
- **AI providers** can be switched at any time via Settings
- **API keys** are stored locally in `config.json` (excluded from version control)
- **Search** is case-insensitive and searches both titles and descriptions
- **Timestamps** use ISO 8601 format for universal compatibility
- **Data persistence** occurs automatically on every modification

---

## Security Best Practices

- **API Keys**: Add `config.json` to `.gitignore` to prevent accidental commits
- **Local Storage**: All task data remains on your machine
- **No Cloud Sync**: Data never leaves your device except for AI API calls

---

## Future Improvements

- [x] AI-powered natural language task creation
- [x] Multi-provider AI support
- [x] Sequential task IDs
- [x] Advanced filtering and search
- [x] Statistics dashboard
- [ ] Task editing (modify existing tasks)
- [ ] Due date tracking with reminders
- [ ] Recurring tasks
- [ ] Subtasks and task dependencies
- [ ] Sort by date or priority
- [ ] Export to CSV or Markdown
- [ ] Color-coded terminal output
- [ ] Task notes and attachments
- [ ] Calendar view
- [ ] Time tracking

---

## Troubleshooting

**"Task not found" errors:**
- Verify the task ID from "View all tasks" (option 2)
- Ensure the task wasn't already deleted
- Task IDs are numbers only (1, 2, 3...)

**AI extraction fails:**
- Check your API key in Settings (option 9)
- Verify you have credits with your AI provider
- Confirm the model name is correct for your provider
- Use manual entry (option 1 → n) if AI continues to fail

**Tasks disappear after restart:**
- Check `tasks.json` exists and has write permissions
- Verify storage path in `config.json` is correct
- Ensure the file isn't corrupted (must be valid JSON)

**Table display issues:**
- Install tabulate: `pip install tabulate`
- Resize terminal window for better formatting
- Ensure terminal supports UTF-8 encoding

**Settings not persisting:**
- Check `config.json` has write permissions
- Verify the file isn't open in another program
- Restart the application after changing settings

---

## Architecture

### Design Patterns
- **Repository Pattern**: Storage abstraction for data persistence
- **Facade Pattern**: TaskManager simplifies complex operations
- **Factory Pattern**: Task.from_dict() for object reconstruction
- **Strategy Pattern**: Interchangeable AI providers
- **Property Pattern**: Validated attribute access

### Data Flow
```
User Input → main.py → TaskManager → Task Objects → storage.py → tasks.json
              ↓
         AI Helper → Provider Client → API → Parse Response
```

### Multi-Provider Support
Each AI provider has a dedicated client module that returns plain text, making it trivial to add new providers:
```python
# Adding a new provider requires:
1. Create ai/new_provider.py with client function
2. Add elif branch in ai_helper.py
3. Configure via Settings menu
```

---

## License

This project is open source and available for personal and educational use.

