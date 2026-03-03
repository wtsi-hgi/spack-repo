# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDefopt(PythonPackage):
    """defopt creates user friendly command line interfaces from type
    annotated Python callables."""

    homepage = "https://github.com/anntzer/defopt"
    pypi = "defopt/defopt-7.0.0.tar.gz"

    license("MIT")

    version("7.0.0", sha256="d7ac98810005880717e1df62527fd35dfe083f551b6d4fb5da0b25f608e8ef4c")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm@6.2:", type="build")

    depends_on("py-docutils@0.12:", type=("build", "run"))
    depends_on("py-sphinxcontrib-napoleon@0.7:", type=("build", "run"))
    depends_on("py-importlib-metadata@1.0:", when="^python@:3.7", type=("build", "run"))
    depends_on("py-typing-inspect@0.8.0:", when="^python@:3.7", type=("build", "run"))
    depends_on("py-pkgutil-resolve-name", when="^python@:3.8", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python("-c", "import defopt")
