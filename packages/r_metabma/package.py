# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabma(RPackage):
	"""Bayesian Model Averaging for Random and Fixed Effects
Meta-Analysis

	Computes the posterior model probabilities for standard meta-analysis models 
    (null model vs. alternative model assuming either fixed- or random-effects, respectively).
    These posterior probabilities are used to estimate the overall mean effect size 
    as the weighted average of the mean effect size estimates of the random- and 
    fixed-effect model as proposed by Gronau, Van Erp, Heck, Cesario, Jonas, & 
    Wagenmakers (2017, <doi:10.1080/23743603.2017.1326760>). The user can define 
    a wide range of non-informative or informative priors for the mean effect size 
    and the heterogeneity coefficient. Moreover, using pre-compiled Stan models, 
    meta-analysis with continuous and discrete moderators with Jeffreys-Zellner-Siow (JZS) 
    priors can be fitted and tested. This allows to compute Bayes factors and 
    perform Bayesian model averaging across random- and fixed-effects meta-analysis 
    with and without moderators. For a primer on Bayesian model-averaged meta-analysis, 
    see Gronau, Heck, Berkhout, Haaf, & Wagenmakers (2021, <doi:10.1177/25152459211031256>).
	"""
	
	homepage = "https://github.com/danheck/metaBMA"
	cran = "metaBMA" 

	version("0.6.9", md5="0eb28a09739c53d68ecd1c72101b5746")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3:", type=("build", "run"))
	depends_on("r-bh@1.78:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
