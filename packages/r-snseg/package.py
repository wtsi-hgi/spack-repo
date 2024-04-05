# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnseg(RPackage):
	"""Self-Normalization(SN) Based Change-Point Estimation for Time
Series

	Implementations self-normalization (SN) based algorithms for 
    change-points estimation in time series data. This comprises nested 
    local-window algorithms for detecting changes in both univariate and 
    multivariate time series developed in Zhao, Jiang and Shao (2022) 
    <doi:10.1111/rssb.12552>.
	"""
	
	cran = "SNSeg" 

	version("1.0.2", md5="81068a6e7ddecc08b5dc71b5feff0522")
	version("1.0.1", md5="eb8b5c007813f92c089adbdee35816f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
