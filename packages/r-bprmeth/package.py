# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBprmeth(RPackage):
	"""Model higher-order methylation profiles

	The BPRMeth package is a probabilistic method to quantify explicit features of methylation profiles, in a way that would make it easier to formally use such profiles in downstream modelling efforts, such as predicting gene expression levels or clustering genomic regions or cells according to their methylation profiles.
	"""
	
	bioc = "BPRMeth" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BPRMeth_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BPRMeth/BPRMeth_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="6ea9cd29c2eaaa669072eba2e9c4135099adbcbb3b4a81b0cc79739113f48945")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
