# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS2dv(RPackage):
	"""A Set of Common Tools for Seasonal to Decadal Verification

	The advanced version of package 's2dverification'. It is 
    intended for 'seasonal to decadal' (s2d) climate forecast verification, but 
    it can also be used in other kinds of forecasts or general climate analysis.  
    This package is specially designed for the comparison between the experimental 
    and observational datasets. The functionality of the included functions covers 
    from data retrieval, data post-processing, skill scores against observation, 
    to visualization. Compared to 's2dverification', 's2dv' is more compatible 
    with the package 'startR', able to use multiple cores for computation and 
    handle multi-dimensional arrays with a higher flexibility. The CDO version used
    in development is 1.9.8.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/es/s2dv/"
	cran = "s2dv" 

	version("2.0.0", md5="ad47ff223180e180d2faed37a1988b82")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-climprojdiags", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-multiapply@2.1.1:", type=("build", "run"))
	depends_on("r-specsverification@0.5:", type=("build", "run"))
	depends_on("r-easyncdf", type=("build", "run"))
	depends_on("r-easyverification", type=("build", "run"))
