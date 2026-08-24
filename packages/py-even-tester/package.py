# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEvenTester(PythonPackage):
    """A python library by srb"""

    homepage = "https://github.com/srbcheema2/even_tester"
    pypi = "even-tester/even_tester-0.0.2.tar.gz"

    version("0.0.1", sha256="9239b2a9197e7f479f3763b140f9254d0ef743c9f93585f73fbe73d78db0b344")
    version("0.0.2", sha256="b3ea5b553f0e182ec754e65b6f845f3024954f709fb49ed6d03c0c38a23d4146")

    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def patch(self):
        filter_file(
            "'console_scripts': [__mod_name__+'='+__mod_name__+'.main']",
            "'console_scripts': []",
            "setup.py",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        python = which(self.spec["python"].command.path)
        python("-c", "import even_tester")
