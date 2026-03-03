# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuberculosis(RPackage):
	"""Tuberculosis Gene Expression Data for Machine Learning

	The tuberculosis R/Bioconductor package features tuberculosis gene expression data for machine learning. All human samples from GEO that did not come from cell lines, were not taken postmortem, and did not feature recombination have been included. The package has more than 10,000 samples from both microarray and sequencing studies that have been processed from raw data through a hyper-standardized, reproducible pipeline.
	"""
	
	homepage = "https://github.com/schifferl/tuberculosis"
	bioc = "tuberculosis" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/tuberculosis_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/tuberculosis/tuberculosis_1.8.0.tar.gz"]

	version("1.8.0", md5="154cd343b8fba727ecf80a671a6a112d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

