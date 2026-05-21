from spack.package import *


class PyDeepvariant(PythonPackage):
    """DeepVariant is a deep learning-based variant caller."""

    homepage = "https://github.com/google/deepvariant"
    url = "https://github.com/google/deepvariant/archive/refs/tags/v1.10.0.tar.gz"
    git = "https://github.com/google/deepvariant.git"

    license("BSD-3-Clause")

    version("1.10.0", sha256="bee56524a4e6da69848c629f34fdb061623c8c3481762bc9ab7b0f05b1e0c537")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("protobuf", type="build")
    depends_on("py-protobuf", type=("build", "run"))

    def patch(self):
        touch("deepvariant/protos/__init__.py")
        touch("third_party/__init__.py")
        filter_file(
            "packages=find_packages(),",
            'packages=find_packages(include=["deepvariant*", "third_party*"]),',
            "setup.py",
            string=True,
        )

    def build(self, spec, prefix):
        python("setup.py", "build_proto")
        super().build(spec, prefix)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import deepvariant")
