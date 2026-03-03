# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for
# details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHatchDocstringDescription(PythonPackage):
    """Hatch metadata hook that extracts the project description from docstrings."""

    homepage = "https://github.com/flying-sheep/hatch-docstring-description"
    pypi = "hatch-docstring-description/hatch_docstring_description-1.1.1.tar.gz"

    license("GPL-3.0-only")

    version("1.1.1", sha256="b15d93c273ba3736abc9e2c542bb42a728a6740703ff5ed85cc072ed49458ae3")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import hatch_docstring_description")
