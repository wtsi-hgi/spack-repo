# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySparse(PythonPackage):
    """This library provides multi-dimensional sparse arrays."""

    homepage = "https://sparse.pydata.org"
    pypi = "sparse/sparse-0.14.0.tar.gz"

    version("0.14.0", sha256="5f5827a37f6cd6f6730a541f994c95c60a3ae2329e01f4ba21ced5339aea0098")
    version("0.11.2", sha256="cadfee8f8bf1d34f76b6559cf6bc2dc4de17ff070666d143ad2cf9507ed80e1f")

    depends_on("python@3.8:", type=("build", "run"), when="@0.14:")
    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-numpy@1.17:", type=("build", "run"), when="@0.14:")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy@0.19:", type=("build", "run"), when="@0.14:")
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-numba@0.49:", type=("build", "run"), when="@0.14:")
    depends_on("py-numba", type=("build", "run"))

    def patch(self):
        if self.spec.satisfies("@0.14"):
            filter_file(
                "configparser.SafeConfigParser()",
                "configparser.ConfigParser()",
                "versioneer.py",
                string=True,
            )
            filter_file("parser.readfp(f)", "parser.read_file(f)", "versioneer.py", string=True)
