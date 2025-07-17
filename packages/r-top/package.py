# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTop(RPackage):
    """TOP Constructs Transferable Model Across Gene Expression Platforms

    TOP constructs a transferable model across gene expression platforms for prospective experiments. Such a transferable model can be trained to make predictions on independent validation data with an accuracy that is similar to a re-substituted model. The TOP procedure also has the flexibility to be adapted to suit the most common clinical response variables, including linear response, binomial and Cox PH models.
    """

    homepage = "https://github.com/Harry25R/TOP"
    bioc = "TOP"

    version("1.8.0", commit="37977c5f4cd4b665bdd65b7ad01ba1b14c017cde")
    version("1.2.0", commit="5f86e64422b72f220aed23ffababc41d35cee4d1")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-classifyr", type=("build", "run"))
    depends_on("r-directpa", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggnewscale", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-ggthemes", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-latex2exp", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidygraph", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
