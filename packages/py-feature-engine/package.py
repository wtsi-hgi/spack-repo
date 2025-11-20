from spack.package import *


class PyFeatureEngine(PythonPackage):
    """Feature engineering and selection package with scikit-learn's fit/transform API."""

    homepage = "https://github.com/feature-engine/feature_engine"
    pypi = "feature-engine/feature_engine-1.9.3.tar.gz"

    version("1.9.3", sha256="7ff8b56e071f22f93c117589a63b8b090d46d138a111edbbf4928dff07c5018b")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-numpy@1.18.2:", type=("build", "run"))
    depends_on("py-pandas@2.2.0:", type=("build", "run"))
    depends_on("py-scikit-learn@1.4.0:", type=("build", "run"))
    depends_on("py-scipy@1.4.1:", type=("build", "run"))
    depends_on("py-statsmodels@0.11.1:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import feature_engine")
