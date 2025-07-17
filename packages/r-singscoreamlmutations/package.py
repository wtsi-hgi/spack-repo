# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingscoreamlmutations(RPackage):
    """Using singscore to predict mutations in AML from transcriptomic signatures

    This workflow package shows how transcriptomic signatures can be used to infer phenotypes. The workflow begins by showing how the TCGA AML transcriptomic data can be downloaded and processed using the TCGAbiolinks packages. It then shows how samples can be scored using the singscore package and signatures from the MSigDB. Finally, the predictive capacity of scores in the context of predicting a specific mutation in AML is shown.The workflow exhibits the interplay of Bioconductor packages to achieve a gene-set level analysis.
    """

    homepage = "https://github.com/DavisLaboratory/SingscoreAMLMutations"
    bioc = "SingscoreAMLMutations"

    version("1.24.0", commit="e554f1e8cf5f93e3c9fce3debb06c38e331ea66e")
    version("1.18.0", commit="ba92d18f3b49a02f27ed438b6096545b499611c6")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-dcanr", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-singscore", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tcgabiolinks", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
