# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCerberus(PythonPackage):
    """Lightweight, extensible schema and data validation tool for Python
    dictionaries."""

    homepage = "https://github.com/pyeve/cerberus"
    pypi = "cerberus/cerberus-1.3.8.tar.gz"

    license("ISC")

    version("1.3.8", sha256="579554887ffd189226774b87570f4a76db75cf0efcbaffcacd5e98b8ee877f61")
    version("1.3.7", sha256="ecf249665400a0b7a9d5e4ee1ffc234fd5d003186d3e1904f70bc14038642c13")
    version("1.3.5", sha256="81011e10266ef71b6ec6d50e60171258a5b134d69f8fb387d16e4936d0d47642")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-importlib-metadata", type=("build", "run"), when="^python@:3.7")

    @run_after("install")
    def install_test(self):
        """Exercise the installed module via an import."""
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import cerberus")
