# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingcar(RPackage):
	"""Comparing Single Cases to Small Samples

	When comparing single cases to control populations and no parameters are known researchers and clinicians must estimate these with a control sample. This is often done when testing a case's abnormality on some variable or testing abnormality of the discrepancy between two variables. Appropriate frequentist and Bayesian methods for doing this are here implemented, including tests allowing for the inclusion of covariates. These have been developed first and foremost by John Crawford and Paul Garthwaite, e.g. in Crawford and Howell (1998) <doi:10.1076/clin.12.4.482.7241>, Crawford and Garthwaite (2005) <doi:10.1037/0894-4105.19.3.318>, Crawford and Garthwaite (2007) <doi:10.1080/02643290701290146> and Crawford, Garthwaite and Ryan (2011) <doi:10.1016/j.cortex.2011.02.017>. The package is also equipped with power calculators for each method. 
	"""
	
	homepage = "https://github.com/jorittmo/singcar"
	cran = "singcar" 

	version("0.1.5", md5="b8cdca3b545fd7558d85c5ff7946d67e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
