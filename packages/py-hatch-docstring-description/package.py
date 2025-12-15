# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHatchDocstringDescription(PythonPackage):
    """Hatchling plugin that reads the project description from the package docstring."""

    homepage = "https://github.com/flying-sheep/hatch-docstring-description"
    pypi = "hatch-docstring-description/hatch_docstring_description-1.1.1.tar.gz"

    license("GPL-3.0-or-later")

    version("1.1.1", sha256="b15d93c273ba3736abc9e2c542bb42a728a6740703ff5ed85cc072ed49458ae3")
    version("1.1", sha256="0380221255d8f2b303035fc4937d9b63d890677564b21d51b766b36863a3c8cf")
    version("1.0.3", sha256="e047997faed9c86725ec88d7574ee208d90998e8d322fb96c485c3d502b26291")
    version("1.0.2", sha256="a21da39911023a3af0a5ec7b2668393111776b420758e89eedc34ecd07ba4afd")
    version("1.0.1", sha256="7a9c22744293d28233d8c0d51c8fe3899ef9b78508cb6da6aa2ff1273d624e13")
    version("1.0", sha256="478a70cb13884f0f2c7f23b1c55b2117df105ff31d8267c74165eb8fb60c8185")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatch-vcs", type="build")
    depends_on("py-hatchling", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import hatch_docstring_description")
