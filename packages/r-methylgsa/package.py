# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylgsa(RPackage):
    """Gene Set Analysis Using the Outcome of Differential Methylation

    The main functions for methylGSA are methylglm and methylRRA. methylGSA implements logistic regression adjusting number of probes as a covariate. methylRRA adjusts multiple p-values of each gene by Robust Rank Aggregation. For more detailed help information, please see the vignette.
    """

    homepage = "https://github.com/reese3928/methylGSA"
    bioc = "methylGSA"

    version("1.26.0", commit="afef6528037e21f03695df3f416b64fafb87309e")
    version("1.20.0", commit="8cb9bb1a13c363aa40d3b331003690de76e31aa9")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-robustrankaggreg", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-missmethyl", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-reactome-db", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
    depends_on("r-illuminahumanmethylationepicanno-ilm10b4-hg19", type=("build", "run"))
