# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaintegration(RPackage):
	"""Ensemble Meta-Prediction Framework

	An ensemble meta-prediction framework to integrate multiple regression 
    models into a current study. Gu, T., Taylor, J.M.G. and Mukherjee, B. (2020) 
    <arXiv:2010.09971>.
    A meta-analysis framework along with two weighted estimators as the ensemble 
    of empirical Bayes estimators, which combines the estimates from the different 
    external models. The proposed framework is flexible and robust in the ways 
    that (i) it is capable of incorporating external models that use a slightly 
    different set of covariates; (ii) it is able to identify the most relevant 
    external information and diminish the influence of information that is less 
    compatible with the internal data; and (iii) it nicely balances the bias-variance 
    trade-off while preserving the most efficiency gain. The proposed estimators 
    are more efficient than the naive analysis of the internal data and other 
    naive combinations of external estimators.
	"""
	
	homepage = "https://github.com/umich-biostatistics/MetaIntegration"
	cran = "MetaIntegration" 

	version("0.1.2", md5="e744b514a34df12052c59909a1eb78df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
