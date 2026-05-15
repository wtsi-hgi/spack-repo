from spack.package import *


class PyConformationalBiasing(PythonPackage):
    """Computational pipeline for designing protein variants with altered
    conformational state preferences from paired structures."""

    homepage = "https://github.com/alicetinglab/ConformationalBiasing"
    url = "https://github.com/alicetinglab/ConformationalBiasing/archive/refs/tags/v1.0.1.tar.gz"
    git = "https://github.com/alicetinglab/ConformationalBiasing.git"

    license("MIT")

    version("1.0.1", sha256="244af56e354ad54c977b2f4769ecbf4eafefe47916cb56a6a628e87ed6c1acc7")
    version("1.0.0", sha256="2759b02769db340c148abc80982ac28b365d5434635b923ac013282453c49f92")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-gemmi", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))

    def patch(self):
        mkdirp("conformational_biasing")
        install("utilities/cbutils.py", "conformational_biasing/cbutils.py")
        touch("conformational_biasing/__init__.py")
        filter_file(
            "^$",
            "from .cbutils import *\n",
            "conformational_biasing/__init__.py",
            string=True,
        )
        with open("setup.py", "w", encoding="utf-8") as fh:
            fh.write(
                'from setuptools import setup\n'
                'setup(\n'
                '    name="conformational-biasing",\n'
                '    version="{0}",\n'
                '    description="Computational pipeline for conformational biasing",\n'
                '    packages=["conformational_biasing"],\n'
                ')\n'.format(self.version)
            )

    @run_after("install")
    def install_test(self):
        python = which(self.spec["python"].command.path)
        with working_dir("spack-test", create=True):
            python("-c", "import conformational_biasing")
