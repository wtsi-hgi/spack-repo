# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSquat(RPackage):
	"""Statistics for Quaternion Temporal Data

	An implementation of statistical tools for the analysis 
    of rotation-valued time series and functional data. It relies on 
    pre-existing quaternion data structure provided by the 'Eigen' 'C++' 
    library.
	"""
	
	homepage = "https://github.com/LMJL-Alea/squat"
	cran = "squat" 

	version("0.3.0", md5="1e732692c7a1cf06619ba56b59141f07")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-fdacluster", type=("build", "run"))
	depends_on("r-fundata", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mfpca", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-roahd", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
