# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RGgeffects(RPackage):
	"""Create Tidy Data Frames of Marginal Effects for 'ggplot' from
Model Outputs

	Compute marginal effects and adjusted predictions from statistical
    models and returns the result as tidy data frames. These data frames are 
    ready to use with the 'ggplot2'-package. Effects and predictions can be 
    calculated for many different models. Interaction terms, splines and 
    polynomial terms are also supported. The main functions are ggpredict(), 
    ggemmeans() and ggeffect(). There is a generic plot()-method to plot the 
    results using 'ggplot2'.
	"""
	
	homepage = "https://strengejacke.github.io/ggeffects/"
	cran = "ggeffects" 

	version("1.3.2", md5="c55ca101a454dcc6011e4b501ce02503")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-insight@0.19.5:", type=("build", "run"))
