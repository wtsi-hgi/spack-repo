# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReslife(RPackage):
	"""Calculate Mean Residual Life (MRL) and Related Values for
Different Distributions

	A pair of functions for calculating mean residual life (MRL)
    , median residual life, and percentile residual life using the outputs of 
    either the 'flexsurv' package or parameters
    provided by the user. Input information about the distribution, the given
    'life' value, the percentile, and the type of residual life, 
    and the function will return your desired values. For the 'flexsurv' option,
    the function allows the user to input their own data for making predictions. 
    This function is based on Jackson (2016) <doi:10.18637/jss.v070.i08>.  
	"""
	
	homepage = "https://github.com/an-crawford/reslife"
	cran = "reslife" 

	version("0.2.1", md5="1e64e098484abc4add53a30730698e28")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
