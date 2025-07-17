# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrena(RPackage):
    """Fit transcriptional regulatory networks using gene expression, priors, machine learning

    Methods for reconstructing transcriptional regulatory networks, especially in species for which genome-wide TF binding site information is available.
    """

    homepage = "https://pricelab.github.io/trena/"
    bioc = "trena"

    version("1.24.0", commit="32af010cc0d111d46684f3fc200b0364496f90be")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-glmnet@2.0.3:", type=("build", "run"))
    depends_on("r-motifdb@1.19.17:", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-rmysql", type=("build", "run"))
    depends_on("r-lassopv", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-xgboost", type=("build", "run"))
    depends_on("r-rpostgresql", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
    depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))
    depends_on("r-snplocs-hsapiens-dbsnp150-grch38", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
