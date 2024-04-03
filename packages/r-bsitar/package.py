# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsitar(RPackage):
	"""Bayesian Super Imposition by Translation and Rotation Growth
Curve Analysis

	The Super Imposition by Translation and Rotation (SITAR) model 
    is a shape-invariant nonlinear mixed effect model that fits a natural cubic 
    spline mean curve to the growth data, and aligns individual-specific growth 
    curves to the underlying mean curve via a set of random effects (see Cole, 
    2010 <doi:10.1093/ije/dyq115> for details). The non-Bayesian version of the 
    SITAR model can be fit by using an already available R package 'sitar'. 
    While 'sitar' package allows modelling of a single outcome only, the 'bsitar' 
    package offers a great flexibility in fitting models of varying complexities 
    that include joint modelling of multiple outcomes such as height and weight 
    (multivariate model). Also, the 'bsitar' package allows simultaneous analysis 
    of a single outcome separately for sub groups defined by a factor variable such 
    as gender. This is achieved by fitting separate models for each sub group 
    (such as males and females for gender variable). An advantage of such approach 
    is that posterior draws for each sub group are part of a single model object 
    that makes it possible to compare coefficients across groups and test hypotheses. 
    As 'bsitar' package is a front-end to the R package 'brms', it offers an excellent 
    support for post-processing of posterior draws via various functions that are 
    directly available from the 'brms' package. In addition, the 'bsitar' package 
    include various customized functions that allow estimation and visualization 
    growth curves such as distance (increase in size with age) and velocity 
    (change in growth rate as a function of age).       
	"""
	
	homepage = "https://github.com/Sandhu-SS/bsitar"
	cran = "bsitar" 

	version("0.1.1", md5="10129a37daac28ca553ed36d398e44f6")
	version("0.2.1", md5="02645d7cf52a61e783488475f5b12789")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-brms@2.17:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-loo@2.7:", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-rlang@1.1.2:", type=("build", "run"))
	depends_on("r-rdpack@2.5:", type=("build", "run"))
	depends_on("r-insight@0.19.7:", type=("build", "run"))
	depends_on("r-marginaleffects@0.18:", type=("build", "run"))
	depends_on("r-sitar", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
