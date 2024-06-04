# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGraphtools(PythonPackage):
    """Tools for building and manipulating graphs in Python.."""

    homepage = "https://github.com/KrishnaswamyLab/graphtools"
    pypi = "graphtools/graphtools-1.5.3.tar.gz"

    version("1.5.3", sha256="b35ae2974d24c507fe01b110d10b1d8c949e20bc49ff9d7d04f94849f9795907")

    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
