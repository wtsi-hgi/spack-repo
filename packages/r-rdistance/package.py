# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdistance(RPackage):
	"""Distance-Sampling Analyses for Density and Abundance Estimation

	Distance-sampling analyses estimate density and 
  abundance of organisms in ecology when detection probability declines with 
  increasing distance from the observers. Distance-sampling is popular 
  in most branches of ecology and especially when 
  organisms are observed from aerial platforms (e.g., airplane or drone), 
  surface vessels (e.g., boat or truck), or along walking transects. 
  Rdistance analyzes data collected on both point and line transects, 
  estimates overall (study area) and site-level (transect or point) 
  density, and allows users to specify regression-like formula (similar 
  to lm or glm) for covariates. A large suite of classical, 
  parametric detection functions are 
  included along with some uncommon parametric 
  functions (e.g., Gamma, negative exponential) and non-parametric
  smoothed distance functions. Custom (user-defined) detection functions
  can be implemented (see vignette).  Measurement unit integrity is 
  enforced with internal unit conversion when necessary. 
  The help files and vignettes have been 
  vetted by multiple authors and tested in workshop 
  settings. 
	"""
	
	homepage = "https://github.com/tmcd82070/Rdistance/wiki"
	cran = "Rdistance" 

	version("3.0.0", md5="e4886b6abd93bcbeaf2b0ce89de926d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
