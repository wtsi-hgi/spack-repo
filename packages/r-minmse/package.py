# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinmse(RPackage):
	"""Implementation of the minMSE Treatment Assignment Method for One
or Multiple Treatment Groups

	Performs treatment assignment for (field) experiments considering available, possibly multivariate and continuous, information (covariates, observable characteristics), that is: forms balanced treatment groups, according to the minMSE-method as proposed by Schneider and Schlather (2017) <DOI:10419/161931>.
	"""
	
	homepage = "https://www.sebastianoschneider.com"
	cran = "minMSE" 

	version("0.5.1", md5="1380bd1c8bad60743287505bc8a8a73b")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
