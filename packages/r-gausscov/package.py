# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGausscov(RPackage):
	"""The Gaussian Covariate Method for Variable Selection

	The standard linear regression theory whether frequentist or Bayesian is based on an 'assumed (revealed?) truth' (John Tukey) attitude to models.  This is reflected in the language of statistical inference which involves a concept of truth, for example confidence intervals, hypothesis testing  and consistency. The motivation behind this package was to remove the word true from the theory and practice of linear regression  and to replace it by approximation. The approximations considered are the least squares approximations. An approximation is called valid if it contains no irrelevant covariates. This is operationalized using the concept of a Gaussian P-value which is the probability that pure Gaussian noise is better in term of least squares than the covariate. The precise definition given in the paper, it  is intuitive and requires only four simple equations. Its overwhelming advantage compared with a standard F P-value is that is is exact and valid whatever the data. In contrast F P-values are only valid for specially designed simulations. Given this a valid approximation is one where all the Gaussian P-values are less than a threshold p0 specified by the statistician, in this package with the default value 0.01. This approximations approach is not only much simpler it is overwhelmingly better than the standard model based approach. The  will be demonstrated using six real data sets, four from high dimensional regression and two from vector autoregression. The simplicity and superiority of Gaussian P-values derive from their universal exactness and validity. This is in complete contrast to standard F P-values which are valid only for carefully designed simulations. The function f1st is the most important function. It is a greedy forward selection procedure which results in either just one or no approximations which may however not be valid. If the size is less than than a threshold with default value 21 then an all subset procedure is called which returns  the best valid subset. A good default start is  f1st(y,x,kmn=15) The best function for returning multiple  approximations is  f3st which repeatedly calls f1st.  For more information see the web site below and the accompanying papers: L. Davies and L. Duembgen, "Covariate Selection Based on a Model-free Approach to Linear Regression with Exact Probabilities", 2022, <arxiv:2202.01553>. L. Davies, "An Approximation Based Theory of Linear Regression", 2024, <arxiv:2402.09858>.
	"""
	
	cran = "gausscov" 

	version("1.1.1", md5="02c9b8252eabfd707b3cd26d36e3abe8")

	depends_on("r@3.5:", type=("build", "run"))
