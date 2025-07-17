# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtrap(RPackage):
    """Identification of candidate causal perturbations from differential gene expression data

    Compare differential gene expression results with those from known cellular perturbations (such as gene knock-down, overexpression or small molecules) derived from the Connectivity Map. Such analyses allow not only to infer the molecular causes of the observed difference in gene expression but also to identify small molecules that could drive or revert specific transcriptomic alterations.
    """

    homepage = "https://nuno-agostinho.github.io/cTRAP"
    bioc = "cTRAP"

    version("1.26.0", commit="ecadc4768fc498b42f7a6a31d5bf70645d52645a")
    version("1.20.1", commit="5b1482190809953077523b1c5d41b94f36cc69fd")
    version("1.20.0", md5="049de878508ce8d8031d7d93f6a1fd01")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-binr", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-fastmatch", type=("build", "run"))
    depends_on("r-fgsea", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-highcharter", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-qs", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-shiny@1.7:", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
