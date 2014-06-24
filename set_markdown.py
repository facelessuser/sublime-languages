import sublime
import sublime_plugin

extensions = [
    "mdown",
    "markdown",
    "markdn",
    "md"
]


class MarkdownSwitcherCommand(sublime_plugin.WindowCommand):
    markdowns = [
        "Markdown",
        "MultiMarkdown",
        "GithubFlavoredMarkdown"
    ]

    def run(self):
        self.window.show_quick_panel(
            self.markdowns,
            self.set_language
        )

    def set_language(self, value):
        if value > -1:
            for x in range(len(self.markdowns)):
                settings = sublime.load_settings("%s.sublime-settings" % self.markdowns[x])
                if value == x:
                    settings.set("extensions", extensions)
                else:
                    settings.set("extensions", [])
                sublime.save_settings("%s.sublime-settings" % self.markdowns[x])
