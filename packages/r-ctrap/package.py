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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cTRAP_1.20.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cTRAP/cTRAP_1.20.1.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.1", sha256="5a1bb2f97ddbe1d7db7925a49cb70690894ebc7633fb0034b2977e0bf0e84433")
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
