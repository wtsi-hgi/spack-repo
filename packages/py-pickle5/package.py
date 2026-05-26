# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPickle5(PythonPackage):
    """This package backports all features and APIs added in the pickle module
    in Python 3.8.3, including the PEP 574 additions. It should work with Python
    3.5, 3.6 and 3.7."""

    homepage = "https://github.com/pitrou/pickle5-backport"
    pypi = "pickle5/pickle5-0.0.11.tar.gz"

    import_modules = ["pickle5"]

    version("0.0.11", sha256="7e013be68ba7dde1de5a8dbcc241f201dab1126e326715916ce4a26c27919ffc")

    depends_on("python@3.5:3.7", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import pickle5")

