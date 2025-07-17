# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpi(RPackage):
    """Molecular Informatics Toolkit for Compound-Protein Interaction in Drug Discovery

    A molecular informatics toolkit with an integration of bioinformatics and chemoinformatics tools for drug discovery.
    """

    homepage = "https://nanx.me/Rcpi/"
    bioc = "Rcpi"

    version("1.44.0", commit="a5056bad8d7bc4bf2fb6640d1dc6ecdaf8ad6f75")
    version("1.38.0", commit="e0262bfaaae14b9dca2b94dbbb308250109edb64")

    depends_on("r@3.0.2:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-gosemsim", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
