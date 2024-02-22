# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpa(RPackage):
	"""Consensus Pathway Analysis

	Provides a set of functions to perform pathway analysis and meta analysis from multiple gene expression datasets, as well as visualization of the results. The package is a wrapper of the following packages: Ritchie et al. (2015) <doi:10.1093/nar/gkv007>, Love et al. (2014) <doi:10.1186/s13059-014-0550-8>, Robinson et al. (2010) <doi:10.1093/bioinformatics/btp616>, Korotkevich et al. (2016) <arxiv:10.1101/060012>, Efron et al. (2015) <https://CRAN.R-project.org/package=GSA>, and Gu, Z. (2012) <https://CRAN.R-project.org/package=CePa>.
	"""
	
	cran = "RCPA" 

	version("0.2.1", md5="b0ced7efaa7011153a7db74ee29cb02b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggpattern", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-robustrankaggreg", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-irdisplay", type=("build", "run"))
