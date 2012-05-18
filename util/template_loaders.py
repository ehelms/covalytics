from django.template.loaders import app_directories, filesystem
from django.template import TemplateDoesNotExist

from hamlpy import hamlpy

class AppLoader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        if not template_name.endswith('.haml'):
            raise TemplateDoesNotExist(template_name)
        
        haml_source, template_path = self.load_template_source(template_name, template_dirs)
        hamlParser = hamlpy.Compiler()
        html = hamlParser.process(haml_source)
            
        return html, template_path

class FileSystemLoader(filesystem.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        if not template_name.endswith('.haml'):
            raise TemplateDoesNotExist(template_name)
        
        haml_source, template_path = self.load_template_source(template_name, template_dirs)
        hamlParser = hamlpy.Compiler()
        html = hamlParser.process(haml_source)
            
        return html, template_path
