# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySouth(PythonPackage):
    """South: Migrations for Django"""

    homepage = "http://south.aeracode.org/"
    pypi = "South/South-1.0.2.tar.gz"

    license("Apache-2.0")

    version("1.0.2", sha256="d360bd31898f9df59f6faa786551065bba45b35e7ee3c39b381b4fbfef7392f4")
    version("1.0.1", sha256="1ce97c634107df324eb2fd53cd904d7c04fc8cc6a8fe0800e5f85345b0c75ad3")
    version("1.0", sha256="017ecc2d66818580e1131af61b8d96901c4a2d05b051186196d9d4f35bdbb901")

    depends_on("py-setuptools@:44.1.1", type="build")
    depends_on("python@2.7:2", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        """Basic import to ensure the Django extension is discoverable."""
        with working_dir("spack-test", create=True):
            python("-c", "import south")
