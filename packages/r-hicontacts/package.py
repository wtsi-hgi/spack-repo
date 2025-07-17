# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicontacts(RPackage):
    """Analysing cool files in R with HiContacts

    HiContacts provides a collection of tools to analyse and visualize Hi-C datasets imported in R by HiCExperiment.
    """

    homepage = "https://github.com/js2264/HiContacts"
    bioc = "HiContacts"

    version("1.10.0", commit="143781ca99fd519507349a1b266efc5a477af08c")
    version("1.4.0", commit="00956df8a2d0e26b22c3ddda7a1f7d55c2e80cb4")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-hicexperiment", type=("build", "run"))
    depends_on("r-interactionset", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocio", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-rspectra", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrastr", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
