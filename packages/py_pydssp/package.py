# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPydssp(PythonPackage):
    """A simplified DSSP implementation for PyTorch and NumPy."""

    homepage = "https://github.com/ShintaroMinami/PyDSSP"
    url = "https://github.com/ShintaroMinami/PyDSSP/archive/refs/tags/v0.9.1.tar.gz"
    license("MIT")

    version("0.9.1", sha256="900328cc4216584ba7b1c1d12e0f870321d02ecd63e20e8a9d7eaac8499815b8")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.20.3:", type=("build", "run"))
    depends_on("py-torch@1.12.1:", type=("build", "run"))
    depends_on("py-einops@0.4.1:", type=("build", "run"))
    depends_on("py-tqdm@4.60:", type=("build", "run"))

    def patch(self):
        filter_file(
            "    use_scm_version={'local_scheme': 'no-local-version'},",
            f"    version='{self.version}',",
            "setup.py",
            string=True,
        )
        filter_file(
            "    setup_requires=['setuptools_scm'],\n",
            "",
            "setup.py",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import pydssp; print(pydssp.__name__)")
