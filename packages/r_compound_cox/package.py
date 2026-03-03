# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompoundCox(RPackage):
	"""Univariate Feature Selection and Compound Covariate for
Predicting Survival

	Univariate feature selection and compound covariate methods under the Cox model with high-dimensional features (e.g., gene expressions).
 Available are survival data for non-small-cell lung cancer patients with gene expressions (Chen et al 2007 New Engl J Med) <DOI:10.1056/NEJMoa060096>,
 statistical methods in Emura et al (2012 PLoS ONE) <DOI:10.1371/journal.pone.0047627>,
 Emura & Chen (2016 Stat Methods Med Res) <DOI:10.1177/0962280214533378>, and Emura et al (2019)<DOI:10.1016/j.cmpb.2018.10.020>.
 Algorithms for generating correlated gene expressions are also available.
 Estimation of survival functions via copula-graphic (CG) estimators is also implemented, which is useful for
 sensitivity analyses under dependent censoring (Yeh et al 2023) <DOI:10.3390/biomedicines11030797>.
	"""
	
	cran = "compound.Cox" 

	version("3.30", md5="e4170dd2d8057f74ae3e89d14586634e")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
