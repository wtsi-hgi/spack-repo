# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLeidenalg(PythonPackage):
    """This package implements the Leiden algorithm in C++ and exposes it to python."""

    pypi = "leidenalg/leidenalg-0.10.1.tar.gz"

    version("0.10.1", sha256="457ad96982a80bd5c657189f42dfeb77eebcd3b744a110e5a2c1618d2eb80b47")

    depends_on("igraph", type=("build", "link"))
    depends_on("libleidenalg", type=("build", "link"))
    depends_on("py-igraph@0.10.0:0.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")
