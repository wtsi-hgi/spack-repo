# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResolve(RPackage):
    """RESOLVE: An R package for the efficient analysis of mutational signatures from cancer genomes

    Cancer is a genetic disease caused by somatic mutations in genes controlling key biological functions such as cellular growth and division. Such mutations may arise both through cell-intrinsic and exogenous processes, generating characteristic mutational patterns over the genome named mutational signatures. The study of mutational signatures have become a standard component of modern genomics studies, since it can reveal which (environmental and endogenous) mutagenic processes are active in a tumor, and may highlight markers for therapeutic response. Mutational signatures computational analysis presents many pitfalls. First, the task of determining the number of signatures is very complex and depends on heuristics. Second, several signatures have no clear etiology, casting doubt on them being computational artifacts rather than due to mutagenic processes. Last, approaches for signatures assignment are greatly influenced by the set of signatures used for the analysis. To overcome these limitations, we developed RESOLVE (Robust EStimation Of mutationaL signatures Via rEgularization), a framework that allows the efficient extraction and assignment of mutational signatures. RESOLVE implements a novel algorithm that enables (i) the efficient extraction, (ii) exposure estimation, and (iii) confidence assessment during the computational inference of mutational signatures.
    """

    homepage = "https://github.com/danro9685/RESOLVE"
    bioc = "RESOLVE"

    version("1.10.0", commit="a607a9318d6993d454b0d30fca45b408e0cf7e55")
    version("1.4.0", commit="52f4592a3c3a71f97ea9dbcbbd2c043453cf2d22")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-1000genomes-hs37d5", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-lsa", type=("build", "run"))
    depends_on("r-mutationalpatterns", type=("build", "run"))
    depends_on("r-nnls", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
