# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultinomineq(RPackage):
	"""Bayesian Inference for Multinomial Models with Inequality
Constraints

	
    Implements Gibbs sampling and Bayes factors for multinomial models with
    linear inequality constraints on the vector of probability parameters. As
    special cases, the model class includes models that predict a linear order 
    of binomial probabilities (e.g., p[1] < p[2] < p[3] < .50) and mixture models 
    assuming that the parameter vector p must be inside the convex hull of a 
    finite number of predicted patterns (i.e., vertices). A formal definition of 
    inequality-constrained multinomial models and the implemented computational
    methods is provided in: Heck, D.W., & Davis-Stober, C.P. (2019). 
    Multinomial models with linear inequality constraints: Overview and improvements 
    of computational methods for Bayesian inference. Journal of Mathematical 
    Psychology, 91, 70-87. <doi:10.1016/j.jmp.2019.03.004>.
    Inequality-constrained multinomial models have applications in the area of 
    judgment and decision making to fit and test random utility models  
    (Regenwetter, M., Dana, J., & Davis-Stober, C.P. (2011). Transitivity of 
    preferences. Psychological Review, 118, 42–56, <doi:10.1037/a0021150>) or to 
    perform outcome-based strategy classification to select the decision strategy 
    that provides the best account for a vector of observed choice frequencies 
    (Heck, D.W., Hilbig, B.E., & Moshagen, M. (2017). From information 
    processing to decisions: Formalizing and comparing probabilistic choice models. 
    Cognitive Psychology, 96, 26–40. <doi:10.1016/j.cogpsych.2017.05.003>).
	"""
	
	homepage = "https://github.com/danheck/multinomineq"
	cran = "multinomineq" 

	version("0.2.6", md5="fb6abc68389f5cc27f207ff1bd625dfa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcppxptrutils", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
