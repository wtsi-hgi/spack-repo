# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImabc(RPackage):
	"""Incremental Mixture Approximate Bayesian Computation (IMABC)

	Provides functionality to perform a likelihood-free method for estimating the parameters of complex models
    that results in a simulated sample from the posterior distribution of model parameters given targets. The method begins
    with a accept/reject approximate bayes computation (ABC) step applied to a sample of points from the prior distribution
    of model parameters. Accepted points result in model predictions that are within the initially specified tolerance
    intervals around the target points. The sample is iteratively updated by drawing additional points from a mixture of
    multivariate normal distributions, accepting points within tolerance intervals. As the algorithm proceeds, the
    acceptance intervals are narrowed. The algorithm returns a set of points and sampling weights that account for the
    adaptive sampling scheme. For more details see Rutter, Ozik, DeYoreo, and Collier (2018) <arXiv:1804.02090>.
	"""
	
	homepage = "https://github.com/carolyner/imabc"
	cran = "imabc" 

	version("1.0.0", md5="53c1c923ede2bc9c1436ebca559686b4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
