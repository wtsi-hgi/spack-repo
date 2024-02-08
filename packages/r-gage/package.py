# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGage(RPackage):
    """GAGE is a widely used method for gene set (enrichment or GSEA) or pathway analysis. """

    #homepage = "https://github.com/datapplab/gage"
    #git = "https://github.com/datapplab/gage"

    bioc = "gage"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/gage_2.52.0.tar.gz"

    version("2.52.0", md5="ffb5ec419d5e08f9b31154202e0e04c8")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))

