# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpidermir(RPackage):
    """SpidermiR: An R/Bioconductor package for integrative network analysis with miRNA data

    The aims of SpidermiR are : i) facilitate the network open-access data retrieval from GeneMania data, ii) prepare the data using the appropriate gene nomenclature, iii) integration of miRNA data in a specific network, iv) provide different standard analyses and v) allow the user to visualize the results. In more detail, the package provides multiple methods for query, prepare and download network data (GeneMania), and the integration with validated and predicted miRNA data (mirWalk, miRTarBase, miRandola, Miranda, PicTar and TargetScan). Furthermore, we also present a statistical test to identify pharmaco-mir relationships using the gene-drug interactions derived by DGIdb and MATADOR database.
    """

    homepage = "https://github.com/claudiacava/SpidermiR"
    bioc = "SpidermiR"

    version("1.32.0", commit="02f4a520fef736f5fcc037a6af87c018f2e7a69a")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-mirnatap", type=("build", "run"))
    depends_on("r-mirnatap-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-gdata", type=("build", "run"))
