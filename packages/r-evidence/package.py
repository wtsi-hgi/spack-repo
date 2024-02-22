# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvidence(RPackage):
	"""Analysis of Scientific Evidence Using Bayesian and Likelihood
Methods

	Bayesian (and some likelihoodist) functions as alternatives to hypothesis-testing functions in R base using a user interface patterned after those of R's hypothesis testing functions. See McElreath (2016, ISBN: 978-1-4822-5344-3), Gelman and Hill (2007, ISBN: 0-521-68689-X) (new edition in preparation) and Albert (2009, ISBN: 978-0-387-71384-7) for good introductions to Bayesian analysis and Pawitan (2002, ISBN: 0-19-850765-8) for the Likelihood approach.  The functions in the package also make extensive use of graphical displays for data exploration and model comparison.
	"""
	
	cran = "evidence" 

	version("0.8.10", md5="27b554f3f3cdd2d73afe9ea7d785eaf9")

	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
