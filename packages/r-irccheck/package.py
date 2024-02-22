# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrccheck(RPackage):
	"""Irrepresentable Condition Check

	Check the irrepresentable condition (IRC) in both L1-regularized regression <doi:10.1109/TIT.2006.883611>
            and Gaussian graphical models. The IRC requires that the important and unimportant variables 
            are not correlated, at least not all that much, and it is necessary for consistent model
            selection. Exploring the IRC as a function of the number of variables, assumed sparsity,
            and effect size can provide valuable insights into the model selection 
            properties of L1-regularization.
	"""
	
	cran = "IRCcheck" 

	version("1.0.0", md5="ef1cc8dadafc99525069eeb989b57525")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggmncv", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
