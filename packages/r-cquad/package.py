# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCquad(RPackage):
	"""Conditional Maximum Likelihood for Quadratic Exponential Models
for Binary Panel Data

	Estimation, based on conditional maximum likelihood, of the quadratic exponential 
             model proposed by Bartolucci, F. & Nigro, V. (2010, Econometrica) <DOI:10.3982/ECTA7531> 
             and of a simplified and a modified version of this model. The quadratic exponential model 
             is suitable for the analysis of binary longitudinal data when state dependence (further 
             to the effect of the covariates and a time-fixed individual intercept) has to be taken 
             into account. Therefore, this is an alternative to the dynamic logit model having the 
             advantage of easily allowing conditional inference in order to eliminate the individual 
             intercepts and then getting consistent estimates of the parameters of main interest 
             (for the covariates and the lagged response). The simplified version of this model 
             does not distinguish, as the original model does, between the last time occasion 
             and the previous occasions. The modified version formulates in a different way the 
             interaction terms and it may be used to test in a easy way state dependence as shown 
             in Bartolucci, F., Nigro, V. & Pigini, C. (2018, Econometric Reviews) <DOI:10.1080/07474938.2015.1060039>. 
             The package also includes estimation of the dynamic logit model by a pseudo conditional 
             estimator based on the quadratic exponential model, as proposed by 
             Bartolucci, F. & Nigro, V. (2012, Journal of Econometrics) <DOI:10.1016/j.jeconom.2012.03.004>. 
             For large time dimensions of the panel, the computation of the proposed models involves a 
             recursive function from Krailo M. D., & Pike M. C. (1984, Journal of the Royal 
             Statistical Society. Series C (Applied Statistics)) and Bartolucci F., Valentini, F. & Pigini C.
             (2021, Computational Economics <DOI:10.1007/s10614-021-10218-2>.
	"""
	
	homepage = "https://cran.r-project.org/package=cquad"
	cran = "cquad" 

	version("2.3", md5="75a344cdcaf82f4dd46616171570f2c7")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
