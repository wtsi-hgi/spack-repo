# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicemd(RPackage):
	"""Multiple Imputation by Chained Equations with Multilevel Data

	Addons for the 'mice' package to perform multiple imputation using chained equations with two-level data. Includes imputation methods dedicated to sporadically and systematically missing values. Imputation of continuous, binary or count variables are available. Following the recommendations of Audigier, V. et al (2018) <doi:10.1214/18-STS646>, the choice of the imputation method for each variable can be facilitated by a default choice tuned according to the structure of the incomplete dataset. Allows parallel calculation and overimputation for 'mice'.
	"""
	
	cran = "micemd" 

	version("1.10.0", md5="1c7671f615c2a90bd587e9baf5fb3453")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mice@2.42:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mvmeta@0.4.7:", type=("build", "run"))
	depends_on("r-jomo@2.6.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-gjrm@0.2.6.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mixmeta", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
