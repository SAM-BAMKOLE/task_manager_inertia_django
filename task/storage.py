from whitenoise.storage import CompressedManifestStaticFilesStorage

class ViteStaticFilesStorage(CompressedManifestStaticFilesStorage):
    def hashed_name(self, name, content=None, filename=None):
        if name.endswith('manifest.json'):
            return name
        return super().hashed_name(name, content, filename)