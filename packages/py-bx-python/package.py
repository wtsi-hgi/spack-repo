# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBxPython(PythonPackage):
    """The bx-python project is a python library and associated set of scripts
    to allow for rapid implementation of genome scale analyses."""

    homepage = "https://github.com/bxlab/bx-python"
    pypi = "bx-python/bx-python-0.8.8.tar.gz"

    version("0.11.0", sha256="2cf8872572817e0d36145cc2711889df5729987ffed4e51280da1e3c2ccb9429")
    version("0.10.0", sha256="bfe9541d7b18a98e907b085e31f58d3989fbca4dc667c4ae48c33b753e0e2da8")
    version("0.9.0", sha256="fe545c44d2ea74b239d41e9090618aaf6a859d1a1f64b4a21b133cb602dfdb49")
    version("0.8.8", sha256="ad0808ab19c007e8beebadc31827e0d7560ac0e935f1100fb8cc93607400bb47")

    depends_on("python@2.7:2.8,3.5:", type=("build", "run"), when="@0.8.8")
    depends_on("python@3.7:", type=("build", "run"), when="@0.10.0:")
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-cython@:1.0.0", when="^python@:2", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("lzo", type=("build", "link"), when="@0.10.0:")
    depends_on("zlib", type=("build", "link"))

    depends_on("python", when="@3.10:")
    depends_on("py-pyparsing", when="@0.11")
