# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgcounts(RPackage):
	"""Calculate 'ActiGraph' Counts from Accelerometer Data

	Calculate 'ActiGraph' counts from the X, Y, and Z axes of a triaxial 
    accelerometer. This work was inspired by Neishabouri et al. who published the 
    article "Quantification of Acceleration as Activity Counts in 'ActiGraph' Wearables" 
    on February 24, 2022. The link to the article (<https://pubmed.ncbi.nlm.nih.gov/35831446>) 
    and 'python' implementation of this code (<https://github.com/actigraph/agcounts>).
	"""
	
	cran = "agcounts" 

	version("0.6.6", md5="c49e49845e0fa9bbfd6e429872a806c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gsignal", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggir", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-read-gt3x", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
