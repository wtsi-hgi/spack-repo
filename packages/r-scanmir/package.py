# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanmir(RPackage):
    """scanMiR

    A set of tools for working with miRNA affinity models (KdModels), efficiently scanning for miRNA binding sites, and predicting target repression. It supports scanning using miRNA seeds, full miRNA sequences (enabling 3' alignment) and KdModels, and includes the prediction of slicing and TDMD sites. Finally, it includes utility and plotting functions (e.g. for the visual representation of miRNA-target alignment).
    """

    bioc = "scanMiR"

    version("1.14.0", commit="806c98f0c815a83fd18f256e9cc2b178e35127f6")
    version("1.8.2", commit="6400e75d52957b3ce4c9963bbcf47818f7e7ee9e")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-seqlogo", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-ggseqlogo", type=("build", "link", "run"))
