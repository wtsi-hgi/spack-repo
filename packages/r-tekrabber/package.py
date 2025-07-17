# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTekrabber(RPackage):
    """An R package estimates the correlations of orthologs and transposable elements between two species

    TEKRABber is made to provide a user-friendly pipeline for comparing orthologs and transposable elements (TEs) between two species. It considers the orthology confidence between two species from BioMart to normalize expression counts and detect differentially expressed orthologs/TEs. Then it provides one to one correlation analysis for desired orthologs and TEs. There is also an app function to have a first insight on the result. Users can prepare orthologs/TEs RNA-seq expression data by their own preference to run TEKRABber following the data structure mentioned in the vignettes.
    """

    homepage = "https://github.com/ferygood/TEKRABber"
    bioc = "TEKRABber"

    version("1.12.0", commit="9d1b124d88cb911738df2d1da7ae75e98b48a693")
    version("1.6.0", commit="af5587ce3fbcc9abe4e02fa40ba8e34e720432c3")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-apeglm", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-scbn", type=("build", "run"))
