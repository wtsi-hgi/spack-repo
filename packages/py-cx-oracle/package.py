# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCxOracle(PythonPackage):
    """Python interface to Oracle"""

    homepage = "https://oracle.github.io/python-cx_Oracle"
    pypi = "cx_Oracle/cx_Oracle-8.3.0.tar.gz"

    version("8.3.0", sha256="3b2d215af4441463c97ea469b9cc307460739f89fdfa8ea222ea3518f1a424d9")
    version("7.3.0", sha256="2e0da54e948b55e5c75fab14b391d58aa8b9be1eddfd9ec9a8a0e500bc8bfc7e")
    # depends_on("c", type="build")  # generated

    depends_on("python@3.6:3.11", type=("build", "run"))
    depends_on("oracle-instant-client")
    depends_on("libaio")
    depends_on("py-setuptools@40.6.0:", type="build")
    depends_on("py-wheel", type="build")

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["oracle-instant-client"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libaio"].prefix.lib)
