# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCageminer(RPackage):
    """Candidate Gene Miner

    This package aims to integrate GWAS-derived SNPs and coexpression networks to mine candidate genes associated with a particular phenotype. For that, users must define a set of guide genes, which are known genes involved in the studied phenotype. Additionally, the mined candidates can be given a score that favor candidates that are hubs and/or transcription factors. The scores can then be used to rank and select the top n most promising genes for downstream experiments.
    """

    homepage = "https://github.com/almeidasilvaf/cageminer"
    bioc = "cageminer"

    version("1.14.0", commit="a1a4142f621fc64eeffef390f6b53bb3468221c4")
    version("1.8.0", commit="31e3906297dde98dc3121fc9ddd5d12b79c0b44c")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-ggtext", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-bionero", type=("build", "run"))
