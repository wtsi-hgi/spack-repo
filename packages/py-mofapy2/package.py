# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMofapy2(PythonPackage):
    """MOFA is a factor analysis model that provides a general framework for the integration of multi-omic data sets in an unsupervised fashion."""

    pypi = "mofapy2/mofapy2-0.7.0.tar.gz"

    version("0.7.0", sha256="b89a5fc7ab68ca2a27332ca51b0882d98c2352977ca106079c5edbc82709ae95")

    depends_on("py-poetry", type=("build", "run"))
