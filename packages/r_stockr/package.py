# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStockr(RPackage):
	"""Identifying Stocks in Genetic Data

	Provides a mixture model for clustering individuals (or sampling groups) into stocks based on their genetic profile. Here, sampling groups are individuals that are sure to come from the same stock (e.g. breeding adults or larvae). The mixture (log-)likelihood is maximised using the EM-algorithm after finding good starting values via a K-means clustering of the genetic data. Details can be found in: Foster, S. D.; Feutry, P.; Grewe, P. M.; Berry, O.; Hui, F. K. C. & Davies (2020) <doi:10.1111/1755-0998.12920>.
	"""
	
	cran = "stockR" 

	version("1.0.76", md5="00fd725402f39d651aff7c7379cbcecd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
