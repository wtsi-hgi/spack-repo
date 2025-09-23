from spack.package import *


class PyBezier(PythonPackage):
    """Helper for Bézier Curves, Triangles, and Higher Order Objects"""

    homepage = "https://github.com/dhermes/bezier"
    pypi = "bezier/bezier-2024.6.20.tar.gz"

    # Provide current and the version pinned by some users
    version("2024.6.20", sha256="0b46357eb6019f969a583093f66e6b73747d5e41c10d9f3dfe327b2aa43dff8c")
    version("2023.7.28", sha256="853256d1e1e9cd82cbb3d1543be906e9d54e8491e3020a90c084a9d18021f63b")
    version("2021.2.12", sha256="d0f752aeb420057ab761f962259c7ca00d925750e324c9bb729f2f10ad39529a")

    # Build/run deps
    # Upstream 2024.6.20 declares support only for Python 3.10–3.12
    depends_on("python@3.10:", when="@2024.6.20:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-numpy", type=("build", "run"))

    # The sdist tries to build a C extension linked to an external 'bezier'
    # C library unless BEZIER_NO_EXTENSION is set. Disable it for portability.
    def setup_build_environment(self, env):
        env.set("BEZIER_NO_EXTENSION", "1")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import bezier")
