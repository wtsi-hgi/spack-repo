# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrend(RPackage):
	"""Trend Estimating Tools

	The traditional linear regression trend, Modified Mann-Kendall (MK)
    non-parameter trend and bootstrap trend are included in this package. Linear 
    regression trend is rewritten by '.lm.fit'. MK trend is rewritten by 'Rcpp'.
    Finally, those functions are about 10 times faster than previous version 
    in R.
    Reference:
    Hamed, K. H., & Rao, A. R. (1998). A modified Mann-Kendall trend test for 
    autocorrelated data. Journal of hydrology, 204(1-4), 182-196. 
    <doi:10.1016/S0022-1694(97)00125-X>.
	"""
	
	homepage = "https://github.com/rpkgs/rtrend"
	cran = "rtrend" 

	version("0.1.5", md5="dad552edfe4f108002c9ad876fff15d8")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fftwtools", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
