# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStpga(RPackage):
	"""Selection of Training Populations by Genetic Algorithm

	Combining Predictive Analytics and Experimental Design to Optimize Results. To be utilized to select a test data calibrated training population in high dimensional prediction problems and assumes that the explanatory variables are observed for all of the individuals. Once a "good" training set is identified, the response variable can be obtained only for this set to build a model for predicting the response in the test set. The algorithms in the package can be tweaked to solve some other subset selection problems. 
	"""
	
	cran = "STPGA" 

	version("5.2.1", md5="fc256dcfc4450477a736f46119659f0f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-algdesign", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-emoa", type=("build", "run"))
