# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDama(RPackage):
    """Efficient design and analysis of factorial two-colour microarray data

    This package contains functions for the efficient design of factorial two-colour microarray experiments and for the statistical analysis of factorial microarray data. Statistical details are described in Bretz et al. (2003, submitted)
    """

    homepage = "http://www.microarrays.med.uni-goettingen.de"
    bioc = "daMA"

    version("1.80.0", commit="bcf9b55eb06fd45c952b0967eb1d4fb5ad6c8182")
    version("1.74.0", commit="9d614e80dc613978e404267f431a712f8d62897b")

    depends_on("r-mass", type=("build", "run"))
