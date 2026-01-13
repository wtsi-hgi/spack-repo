# Copyright 2013-2025 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythonDotenv(PythonPackage):
    """Read key-value pairs from a .env file and set them as environment variables."""

    homepage = "https://github.com/theskumar/python-dotenv"
    pypi = "python-dotenv/python_dotenv-1.2.1.tar.gz"

    license("BSD-3-Clause")

    version("1.2.1", sha256="42667e897e16ab0d66954af0e60a9caa94f0fd4ecf3aaf6d2d260eec1aa36ad6")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-click@5:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            dotenv_cli = Executable(join_path(self.prefix.bin, "dotenv"))
            dotenv_cli("--help")

            python = self.spec["python"].command
            python("-c", "import dotenv")
