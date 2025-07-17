# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtrachips(RPackage):
    """Additional functions for working with ChIP-Seq data

    This package builds on existing tools and adds some simple but extremely useful capabilities for working wth ChIP-Seq data. The focus is on detecting differential binding windows/regions. One set of functions focusses on set-operations retaining mcols for GRanges objects, whilst another group of functions are to aid visualisation of results. Coercion to tibble objects is also included.
    """

    homepage = "https://github.com/smped/extraChIPs"
    bioc = "extraChIPs"

    version("1.12.0", commit="73770eea0d1832812235f5f5fbd35f3c04430f18")
    version("1.6.1", commit="fb27d0b4aeac210ee5a27865e339567211b65250")

    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2@3.5:", type=("build", "run"))
    depends_on("r-ggside@0.3:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-biocio", type=("build", "run"))
    depends_on("r-broom", type=("build", "run"))
    depends_on("r-complexupset", type=("build", "run"))
    depends_on("r-csaw", type=("build", "run"))
    depends_on("r-dplyr@1.1.1:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-enrichedheatmap", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicinteractions", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-interactionset", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-venndiagram", type=("build", "run"))
