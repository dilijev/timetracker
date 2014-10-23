This program will be a command line application, written in Python, which will allow users to keep track of the time spent on various tasks as they work on projects.

Since my primary workflow has to do with balancing several different classes worth of school work, often working on multiple assignments or projects at once, task groups can be created (such as for classes), and then tasks are created within the task groups.

When created, tasks can be given an estimated time to completion. When a user starts work on a task, the time started will be logged. At any time while working on a task a user can query the current status which will show the user the currently active task, how much time has been logged in this session, and how much time has been logged overall for this task.

Users can set the estimated time to completion at any time. Perhaps this could be an argument to the command which allows a user to mark a session on a task as ended, but let's keep it simple for now.

Times associated with a task should be:

- time created
- original estimate
- time logged (no reason to separate this from total time) -- also tasks can be eopened
- estimated time remaining (optional)

I'm not sure yet how the sessions should be kept... whether they should be kept as lists within the tasks themselves, or whether they should be kept in a time-linear list which can be searched through for sessions related to a task. I think the latter would make more sense, but would potentially get slow as more and more sessions are logged. 

Other information associated with a task should be whether the task is active or completed. Completed tasks should be kept around because they can be reopened to continue work if more work needs to be done, and so that logs can be considered for each task to analyze how long something took, whether that time was well-spent, etc.


## Best practices

Don't actually log the time spent not working unless it is a significant category where time can end up being spent (and is significant for logging), rather than simply time spent doing nothing.


## Commands

At least as I would like them to be, maybe. The goal is to make a state machine where all of the state and data is saved to and loaded from files, a la git. The goal of the state is to make operations more organic and to prevent making mistakes which would be made with complicated commands. The goal is also to prevent a user from having to launch a program and then track time via a REPL. The user should still be allowed to be productive on the command line while using this tool (which has no need to be running continuously anyway).

    tt status

Shows the current state of the system, as well as any information that a user might want to see by default. This includes information about the active sessiona and task.

    tt report [-g|--group]

Show a report for the day (starting and ending at midnight by default).
By default, show it in order of time, and show a summary of the total time in each task and group, and overall work time.
If --group is specified, then show sessions grouped by task, which are also grouped by task group, and show a summary of the total time in each category in line with this report, instead of at the end.

    tt group [-h|--help]

With no arguments or with the -help argument, lists the commands available for group management.

    tt group groupname

Switch to the task group identified by groupname.

    tt group [[-c|--create] groupname]

Create a task group named groupname.

    tt groups

List the task groups available.

    tt tasks [-a|--active] [-d|--done] [--all]

List the tasks active in the current group.
With --active, shows only the active tasks in the current group. This is the default, and doesn't need to be implemented unless there is a way to override the default behavior.
With --done, shows only the completed/done tasks in the group.
With --all, shows all the tasks in the current group.

    tt task

Shows commands available for task.

    tt task [[-c|--create] taskname]

Create a task named taskname.

    tt start [taskname]

Start a session logging the specified task. If no task is given, start the most recently created or logged task.

    tt cancel

Cancel the active session /  logging operation, throwing away the log for the session.

    tt stop

Stop logging the current session and save the log permanently.
