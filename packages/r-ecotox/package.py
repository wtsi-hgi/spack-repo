# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcotox(RPackage):
	"""Analysis of Ecotoxicology

	A simple approach to using a probit or logit analysis to calculate
        lethal concentration (LC) or time (LT) and the appropriate fiducial 
        confidence limits desired for selected LC or LT for
        ecotoxicology studies (Finney 1971; Wheeler et al. 2006; 
        Robertson et al. 2007). The simplicity of 'ecotox' comes from the 
        syntax it implies within its functions which are similar to functions 
        like glm() and lm(). In addition to the simplicity of the syntax, 
        a comprehensive data frame is produced which gives the user a 
        predicted LC or LT value for the desired level and a suite of important 
        parameters such as fiducial confidence limits and slope.   
        Finney, D.J. (1971, ISBN: 052108041X);
        Wheeler, M.W., Park, R.M., and Bailer, A.J. (2006) <doi:10.1897/05-320R.1>;
        Robertson, J.L., Savin, N.E., Russell, R.M., and Preisler, H.K.
        (2007, ISBN: 0849323312).
	"""
	
	cran = "ecotox" 

	version("1.4.4", md5="f20c4d0eeb618955f29eff0b64fa8a00")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
