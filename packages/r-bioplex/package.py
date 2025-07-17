# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioplex(RPackage):
    """R-side access to BioPlex protein-protein interaction data

    The BioPlex package implements access to the BioPlex protein-protein interaction networks and related resources from within R. Besides protein-protein interaction networks for HEK293 and HCT116 cells, this includes access to CORUM protein complex data, and transcriptome and proteome data for the two cell lines. Functionality focuses on importing the various data resources and storing them in dedicated Bioconductor data structures, as a foundation for integrative downstream analysis of the data.
    """

    homepage = "https://github.com/ccb-hms/BioPlex"
    bioc = "BioPlex"

    version("1.14.0", commit="b4d955d57546b5b6e490d5c5f5cdfc8814848a7e")
    version("1.8.0", commit="0fe8113b2e56e9fa8e55a3ff95128162e9902aea")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
