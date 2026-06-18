# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCradle(PythonPackage):
    """Correct Read Counts and Analysis of Differently Expressed Regions"""

    homepage = "https://github.com/ReddyLab/CRADLE"
    pypi = "CRADLE/CRADLE-0.30.0.tar.gz"

    license("MIT")

    version("0.19.0", sha256="e35b3f9feef5045d22011d8b4062cea5696d09750c4cd48cf8de412978c4b8d5")
    version("0.24.0", sha256="e2580add8badd7068210cc22702de94fb254a92bab4b1b9fe9a07bd476b739a6")
    version("0.24.2", sha256="a93934e29e2918a2373220a93e617d5c1343f4256a8f33aecbfcd2ee79d77a58")
    version("0.25.1", sha256="3c8e350e6f75dc2d1a1c985354070c40ddcee8db0bf4943d5aee5b2aa1052dbc")
    version("0.26.1", sha256="080412fea43a31293453ba59297f5f47dc0fba8981ebb22d2d25cdbf2f14b55e")
    version("0.27.0", sha256="c14614f1a6b31b5564ad9b986e775bb0d7b7361b77d813681738d79f1c008876")
    version("0.28.0", sha256="2683d6aad3017d0ca901073d29939e92895f242cc771b031c3ba93862044afa1")
    version("0.29.0", sha256="838b5bb19fd4a998057f9252d1ba105576dc7d224e550d631a945276581cfbf1")
    version("0.30.0", sha256="f1fba4a23779570e2fc58d9d93a6aacdf83349dac85a3c8d91d24e7de4069499")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.14.3:", type=("build", "run"))
    depends_on("py-argparse@1.1:", type=("build", "run"))
    depends_on("py-py2bit@0.3.0:", type=("build", "run"))
    depends_on("py-pybigwig@0.3.11:", type=("build", "run"))
    depends_on("py-statsmodels@0.8.0:", type=("build", "run"))
    depends_on("py-scipy@1.0.1:", type=("build", "run"))
    depends_on("py-matplotlib@1.5.3:", type=("build", "run"))
    depends_on("py-h5py@2.6.0:", type=("build", "run"))
    depends_on("py-cython@0.24.1:", type="build")

    def setup_build_environment(self, env):
        """Ensure BLAS libraries are discoverable when numpy initializes."""
        if "blas" in self.spec:
            for libdir in self.spec["blas"].libs.directories:
                env.prepend_path("LD_LIBRARY_PATH", libdir)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import CRADLE")
