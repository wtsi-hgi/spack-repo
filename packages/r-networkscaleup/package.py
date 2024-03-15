# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkscaleup(RPackage):
	"""Network Scale-Up Models for Aggregated Relational Data

	Provides a variety of Network Scale-up Models for researchers to analyze Aggregated Relational Data, mostly through the use of Stan. In this version, the package implements models from Laga, I., Bao, L., and Niu, X (2021) <arXiv:2109.10204>, Zheng, T., Salganik, M. J., and Gelman, A. (2006) <doi:10.1198/016214505000001168>, Killworth, P. D., Johnsen, E. C., McCarty, C., Shelley, G. A., and Bernard, H. R. (1998) <doi:10.1016/S0378-8733(96)00305-X>, and Killworth, P. D., McCarty, C., Bernard, H. R., Shelley, G. A., and Johnsen, E. C. (1998) <doi:10.1177/0193841X9802200205>.
	"""
	
	cran = "networkscaleup" 

	version("0.1-2", md5="fd983e327daef2531586a42d78833eb3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-laplacesdemon@16.1.6:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
