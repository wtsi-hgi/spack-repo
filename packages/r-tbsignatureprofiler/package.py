# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbsignatureprofiler(RPackage):
    """Profile RNA-Seq Data Using TB Pathway Signatures

    Gene signatures of TB progression, TB disease, and other TB disease states have been validated and published previously. This package aggregates known signatures and provides computational tools to enlist their usage on other datasets. The TBSignatureProfiler makes it easy to profile RNA-Seq data using these signatures and includes common signature profiling tools including ASSIGN, GSVA, and ssGSEA. Original models for some gene signatures are also available.  A shiny app provides some functionality alongside for detailed command line accessibility.
    """

    homepage = "https://github.com/compbiomed/TBSignatureProfiler"
    bioc = "TBSignatureProfiler"

    version("1.20.0", commit="8aaba5a59d9bcfde043cdd443850479548492191")
    version("1.14.0", commit="373e8f159a71f7c90c9b46d0556e8e8b1f68c718")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-assign@1.23.1:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-gdata", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gsva", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rocit", type=("build", "run"))
    # Additional dependencies required at build time by upstream package
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-hgnchelper", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-singscore", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r@4.4.0:", when="@1.20.0:", type=("build", "run"))
