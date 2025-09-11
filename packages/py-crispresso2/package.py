from spack.package import *


class PyCrispresso2(PythonPackage):
    """CRISPResso2: analysis of genome editing outcomes from sequencing data.

    Provides CLI tools like `CRISPResso`, `CRISPRessoBatch`, `CRISPRessoWGS`,
    etc., implemented in Python with Cython extensions.
    """

    homepage = "https://github.com/pinellolab/CRISPResso2"
    url = "https://github.com/pinellolab/CRISPResso2/archive/refs/tags/v2.3.3.tar.gz"

    # Upstream uses a custom EULA for academic use
    license("LicenseRef-Proprietary")

    version("2.3.3", sha256="9570bfb9257677b7581a6b1ec59ddb57fb53aca438c916f29b0a3332854e09db")

    # Optional runtime helpers/tools
    variant("plotly", default=False, description="Enable interactive plotting via plotly")
    variant("fastp", default=False, description="Enable fastp for read preprocessing")
    variant("bowtie2", default=False, description="Enable bowtie2 for alignment-heavy workflows")
    variant("samtools", default=False, description="Enable samtools for BAM/CRAM utilities")

    # Build requirements from pyproject.toml
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-numpy", type=("build", "run"))

    # Runtime requirements from pyproject.toml/setup.py
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    # Optional runtime dependencies (gated behind variants)
    depends_on("py-plotly", when="+plotly", type=("build", "run"))
    depends_on("fastp", when="+fastp", type="run")
    depends_on("bowtie2", when="+bowtie2", type="run")
    depends_on("samtools", when="+samtools", type="run")

    @run_after("install")
    def install_test(self):
        # Prefer a CLI smoke test; fall back to import if not available
        with working_dir("spack-test", create=True):
            try:
                # The main entry point should print help and exit
                Executable("CRISPResso")("-h")
            except Exception:
                # Fallback basic import test
                python = Executable(self.spec["python"].command.path)
                python("-c", "import CRISPResso2")

