import re
import sublime
import sublime_plugin
import subprocess


class SimpleImportCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected = self.view.substr(self.view.sel()[0])
        current_file = self.view.file_name()
        settings = sublime.load_settings("SimpleImport.sublime-settings")
        config = settings.get('config', {})
        root_path = ''
        for key, value in config.items():
            if key in current_file:
                root_path = key
                break
        if not root_path:
            return
        omit_path_prefixes = config[root_path]['omit_path_prefixes']
        search = u'(def|class) '+selected+u'\('
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
        for path in omit_path_prefixes:
            if path in filepath:
                if len(path) > idx:
                    idx = len(path)+1
                    trunc_filepath = filepath[idx:]
        import_path = trunc_filepath.replace('/', '.')
        import_mssg = 'from ' + import_path + ' import ' + selected + '\n'
        self.view.insert(edit, 0, import_mssg)
