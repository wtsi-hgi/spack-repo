from spack.package import *


class PyScprinter(PythonPackage):
    """scPrinter provides multiscale footprinting utilities for single-cell
    chromatin accessibility analysis."""

    homepage = "https://github.com/buenrostrolab/scPrinter"
    git = "https://github.com/buenrostrolab/scPrinter.git"
    url = "https://github.com/buenrostrolab/scPrinter/archive/refs/tags/v1.2.0.tar.gz"

    license("MIT")

    import_modules = ["scprinter"]

    version("1.2.0", sha256="ceaf033c83b961126698c642ce51e65a5b49571f8e92908be39ad33e41fc7022")
    version("1.1.2", sha256="22ef0544f5338967a3454ce7542030ede6c4a217d2bac7e247d4b7957f800a24")

    depends_on("python@3.8:3.12", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-bioframe", type=("build", "run"))
    depends_on("py-torch~cuda~distributed~rocm", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pyranges", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-moods-python", type=("build", "run"))
    depends_on("py-snapatac2", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-dna-features-viewer", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-gffutils", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))
    depends_on("py-logomaker", type=("build", "run"))
    depends_on("py-shap", type=("build", "run"))
    depends_on("py-tangermeme", type=("build", "run"))
    depends_on("py-adjusttext", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))

    def patch(self):
        filter_file(
            'dynamic = ["version"]',
            'version = "{0}"'.format(self.version),
            "pyproject.toml",
            string=True,
        )
        filter_file(
            '[tool.hatch.version]\nsource = "vcs"\n',
            "",
            "pyproject.toml",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import scprinter")
