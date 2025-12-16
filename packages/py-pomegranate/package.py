# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPomegranate(PythonPackage):
    """Fast, flexible and easy to use probabilistic modelling in Python."""

    homepage = "https://github.com/jmschrei/pomegranate"
    pypi = "pomegranate/pomegranate-0.12.0.tar.gz"

    license("MIT")

    version("0.12.0", sha256="8b00c88f7cf9cad8d38ea00ea5274821376fefb217a1128afe6b1fcac54c975a")

    # depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    # This legacy Cython-based release fails with Cython 3.x (compiler crash during egg_info).
    # Pin to a known-good Cython in the 0.29 series.
    depends_on("py-cython@0.29.36", type="build")
    conflicts("^py-cython@3:", msg="pomegranate 0.12.0 is incompatible with Cython 3.x")
    # NumPy 2.x breaks compilation for this old Cython-based release.
    depends_on("py-numpy@1.8.0:1", type=("build", "run"))
    depends_on("py-joblib@0.9.0b4:", type=("build", "run"))
    depends_on("py-networkx@2.0:", type=("build", "run"))
    depends_on("py-scipy@0.17.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))

    def patch(self):
        # setup.py tries to do `__builtins__.__NUMPY_SETUP__ = False`, but under
        # setuptools' exec() path `__builtins__` can be a *dict* (Python 3),
        # causing `AttributeError: 'dict' object has no attribute '__NUMPY_SETUP__'`
        # during metadata generation.
        filter_file(
            r"__builtins__\.__NUMPY_SETUP__ = False",
            "import builtins\n        builtins.__NUMPY_SETUP__ = False",
            "setup.py",
        )

    def setup_build_environment(self, env):
        # Ensure we use the pinned Cython (0.29.x), even if other deps (e.g. SciPy)
        # bring a newer Cython into the build DAG.
        env.prepend_path("PATH", self.spec["py-cython"].prefix.bin)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import pomegranate")
