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

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    with default_args(type=("build", "run")): 
        depends_on("python@3.8:3.12")
        depends_on("py-numpy")
        depends_on("py-h5py")
        depends_on("py-pandas")
        depends_on("py-scipy")
        depends_on("py-bioframe")
        depends_on("py-torch~cuda~distributed~rocm")
        depends_on("py-pybedtools")
        depends_on("py-pyranges")
        depends_on("py-biopython")
        depends_on("py-moods-python")
        depends_on("py-snapatac2")
        depends_on("py-plotly")
        depends_on("py-dna-features-viewer")
        depends_on("py-scanpy")
        depends_on("py-pybigwig")
        depends_on("py-gffutils")
        depends_on("py-wandb")
        depends_on("py-logomaker")
        depends_on("py-shap")
        depends_on("py-tangermeme@:0.4")
        depends_on("py-adjusttext")
        depends_on("py-anndata")
        depends_on("py-pysam")
        depends_on("py-pyfaidx")
        depends_on("py-tqdm")
        depends_on("py-statsmodels")
        depends_on("py-typing-extensions")

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
