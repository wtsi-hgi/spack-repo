from spack.package import *


class RMariaosmalaTfbs(Package):
    """Transcription factor motif and binding site analysis resources.

    Repository containing motif collections, workflow scripts, and environment
    descriptions used for transcription factor motif and binding site analyses.
    """

    homepage = "https://github.com/MariaOsmala/TFBS"
    git = "https://github.com/MariaOsmala/TFBS.git"
    url = "https://github.com/MariaOsmala/TFBS/archive/refs/tags/v1.0.0.tar.gz"

    license("MIT")

    version("1.0.0", sha256="d748376f36016ed8a14d1be2560a40b7de794a2e3ef64467e5e124ad9aa1bb30")

    def install(self, spec, prefix):
        install_tree(".", prefix.share.tfbs)

    def setup_run_environment(self, env):
        env.set("MARIAOSMALA_TFBS_HOME", self.prefix.share.tfbs)
