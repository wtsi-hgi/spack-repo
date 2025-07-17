# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZenith(RPackage):
    """Gene set analysis following differential expression using linear (mixed) modeling with dream

    Zenith performs gene set analysis on the result of differential expression using linear (mixed) modeling with dream by considering the correlation between gene expression traits.  This package implements the camera method from the limma package proposed by Wu and Smyth (2012).  Zenith is a simple extension of camera to be compatible with linear mixed models implemented in variancePartition::dream().
    """

    homepage = "https://DiseaseNeuroGenomics.github.io/zenith"
    bioc = "zenith"

    version("1.10.0", commit="4167305d9fd4dd4e453b53c3dc2c7330fc27f495")
    version("1.4.2", commit="cd2b22f46e19b8745cbd402d2f1ec196617d1acc")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-variancepartition@1.26:", type=("build", "run"))
    depends_on("r-enrichmentbrowser@2.22:", type=("build", "run"))
    depends_on("r-gseabase@1.54:", type=("build", "run"))
    depends_on("r-msigdbr@7.5.1:", type=("build", "run"))
    depends_on("r-rfast", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
