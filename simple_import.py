import re
import sublime
import sublime_plugin
import subprocess


class SimpleImportCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("SimpleImport.sublime-settings")
        root_path = settings.get('root_path', '')
        search_paths = settings.get('search_paths', [])
        if not root_path:
            return
        selected = self.view.substr(self.view.sel()[0])
        search = '(def|class) '+selected+'\('
        out = subprocess.Popen(['rg', '-r', '-i', search, root_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        stdout_str = stdout.decode('utf-8')
        stdout_str = stdout_str.rstrip()
        if not stdout_str:
            import_mssg = 'import ' + selected + '\n'
            self.view.insert(edit, 0, import_mssg)
            return
        filepath = re.sub(r'[\.].*', '', stdout_str)
        trunc_filepath = ''
        idx = 0
        for path in search_paths:
            if path in filepath:
                if len(path) > idx:
                    idx = len(path)+1
                    trunc_filepath = filepath[idx:]
        import_path = trunc_filepath.replace('/', '.')
        import_mssg = 'from ' + import_path + ' import ' + selected + '\n'
        self.view.insert(edit, 0, import_mssg)
