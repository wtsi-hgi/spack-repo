# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyright(PythonPackage):
    """Pyright for Python is a Python command-line wrapper over pyright, a static type checker for Python."""

    homepage = "https://github.com/RobertCraigie/pyright-python"
    pypi = "pyright/pyright-1.1.336.tar.gz"

    version("1.1.336", sha256="f92d6d6845e4175833ea60dee5b1ef4d5d66663438fdaedccc1c3ba0f8efa3e3")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
