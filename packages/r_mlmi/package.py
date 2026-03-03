# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmi(RPackage):
	"""Maximum Likelihood Multiple Imputation

	Implements so called Maximum Likelihood Multiple Imputation as described by von Hippel and Bartlett (2021) <doi:10.1214/20-STS793>. A number of different imputations are available, by utilising the 'norm', 'cat' and 'mix' packages. Inferences can be performed either using combination rules similar to Rubin's or using a likelihood score based approach based on theory by Wang and Robins (1998) <doi:10.1093/biomet/85.4.935>.
	"""
	
	cran = "mlmi" 

	version("1.1.2", md5="71fea7090fa582113196a589f23f6ac8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-cat", type=("build", "run"))
	depends_on("r-mix", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
