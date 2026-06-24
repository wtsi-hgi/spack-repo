# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTox(PythonPackage):
    """tox is a generic virtualenv management and test command line tool."""

    homepage = "https://tox.readthedocs.org/"
    pypi = "tox/tox-3.14.2.tar.gz"

    version("4.0.19", sha256="31d95663dc66f8d53fdf0825f1fc931404b1db5380482c5449628f49db767047")
    version("3.14.2", sha256="7efd010a98339209f3a8292f02909b51c58417bfc6838ab7eca14cf90f96117a")

    with when("@3"):
        depends_on("python@2.7:2.8,3.5:", type=("build", "run"))
        depends_on("py-setuptools", type=("build", "run"))
        depends_on("py-importlib-metadata@1.1.0:", when="^python@:3.7", type=("build", "run"))
        depends_on("py-packaging@14:", type=("build", "run"))
        depends_on("py-pluggy@0.12.0:0", type=("build", "run"))
        depends_on("py-py@1.4.17:1", type=("build", "run"))
        depends_on("py-six@1.0.0:1", type=("build", "run"))
        depends_on("py-virtualenv@16.0.0:", type=("build", "run"))
        depends_on("py-toml@0.9.4:", type=("build", "run"))
        depends_on("py-filelock@3.0.0:3", type=("build", "run"))

    with when("@4:"):
        depends_on("py-cachetools@5.2:", type=("build", "run"))
        depends_on("py-chardet@5.1:", type=("build", "run"))
        depends_on("py-colorama@0.4.6:", type=("build", "run"))
        depends_on("py-packaging@22:", type=("build", "run"))
        depends_on("py-platformdirs@2.6:", type=("build", "run"))
        depends_on("py-pluggy@1:", type=("build", "run"))
        depends_on("py-pyproject-api@1.2.1:", type=("build", "run"))
        depends_on("py-tomli@2.0.1:", type=("build", "run"), when="^python@:3.11")
        depends_on("py-virtualenv@20.17.1:", type=("build", "run"))
        depends_on("py-filelock@3.8.2:", type=("build", "run"))
        depends_on("py-importlib-metadata@5.2", type=("build", "run"), when="^python@:3.8")
        depends_on("py-typing-extensions@4.4:", type=("build", "run"), when="^python@:3.8")
        depends_on("py-hatchling@1.29:", type=("build", "run"))
        depends_on("py-hatch-vcs@0.5:", type=("build", "run"))
