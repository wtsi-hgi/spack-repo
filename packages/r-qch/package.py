# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQch(RPackage):
	"""Query Composed Hypotheses

	Provides functions for the joint analysis of K sets
    of p-values obtained for a same list of items. This joint analysis is
    performed by querying a composed hypothesis, i.e. an arbitrary complex
    combination of simple hypotheses, as described in Mary-Huard et al.
    (2021) <arXiv:2104.14601>. The null distribution corresponding to the
    composed hypothesis of interest is obtained by fitting non-parametric
    mixtures models (one for each of the simple hypothesis of the complex
    combination). Type I error rate control is achieved through Bayesian
    False Discovery Rate control.  The 3 main functions of the package
    GetHinfo(), qch.fit() and qch.test() correspond to the 3 steps for
    querying a composed hypothesis (composed H0/H1 formulation, inferring
    the null distribution and testing the null hypothesis).
	"""
	
	cran = "qch" 

	version("1.0.0", md5="f7f15061b0a4822b6fd5698c16094728")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
