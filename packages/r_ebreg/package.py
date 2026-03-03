# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbreg(RPackage):
	"""Implementation of the Empirical Bayes Method

	Implements a Bayesian-like approach to the high-dimensional sparse linear regression problem based on an empirical or data-dependent prior distribution, which can be used for estimation/inference on the model parameters, variable selection, and prediction of a future response. The method was first presented in Martin, Ryan and Mess, Raymond and Walker, Stephen G (2017) <doi:10.3150/15-BEJ797>. More details focused on the prediction problem are given in Martin, Ryan and Tang, Yiqi (2019) <arXiv:1903.00961>.
	"""
	
	cran = "ebreg" 

	version("0.1.3", md5="832f2a140f612d4f8e2f2a4c979b5588")

	depends_on("r-lars", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
