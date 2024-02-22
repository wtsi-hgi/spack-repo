# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClubsandwich(RPackage):
	"""Cluster-Robust (Sandwich) Variance Estimators with Small-Sample
Corrections

	Provides several cluster-robust variance estimators (i.e.,
    sandwich estimators) for ordinary and weighted least squares linear regression
    models, including the bias-reduced linearization estimator introduced by Bell
    and McCaffrey (2002) 
    <https://www150.statcan.gc.ca/n1/pub/12-001-x/2002002/article/9058-eng.pdf> and 
    developed further by Pustejovsky and Tipton (2017) 
    <DOI:10.1080/07350015.2016.1247004>. The package includes functions for estimating
    the variance- covariance matrix and for testing single- and multiple-
    contrast hypotheses based on Wald test statistics. Tests of single regression
    coefficients use Satterthwaite or saddle-point corrections. Tests of multiple-
    contrast hypotheses use an approximation to Hotelling's T-squared distribution.
    Methods are provided for a variety of fitted models, including lm() and mlm
    objects, glm(), geeglm() (from package 'geepack'), ivreg() (from package 'AER'), ivreg() (from package 'ivreg' when 
    estimated by ordinary least squares), plm() (from package 'plm'), gls() and 
    lme() (from 'nlme'), lmer() (from `lme4`), robu() (from 'robumeta'), and rma.uni() 
    and rma.mv() (from 'metafor').
	"""
	
	homepage = "http://jepusto.github.io/clubSandwich/"
	cran = "clubSandwich" 

	version("0.5.10", md5="e1902cb9a93ccf46f1eedf96396280d9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
