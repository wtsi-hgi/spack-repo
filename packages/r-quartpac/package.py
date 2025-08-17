# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuartpac(RPackage):
    """Identification of mutational clusters in protein quaternary structures.

    Identifies clustering of somatic mutations in proteins over the entire quaternary structure.
    """

    bioc = "QuartPAC"

    version("1.40.0", commit="d81b6b0839e1b77bfc9ef6e9ed7db17c163764b1")
    version("1.34.0", commit="53f4553885babcc0a047027987e5fdd56267895c")

    depends_on("r-ipac", type=("build", "run"))
    depends_on("r-graphpac", type=("build", "run"))
    depends_on("r-spacepac", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    # Upstream DESCRIPTION lists 'pwalign'
    depends_on("r-pwalign", type=("build", "run"))
