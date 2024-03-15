# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvst(RPackage):
	"""Bayesian Inference for the Multivariate Skew-t Model

	Estimates the multivariate skew-t and nested models, as described in the
    articles Liseo, B., Parisi, A. (2013). Bayesian inference for the multivariate skew-normal
    model: a population Monte Carlo approach. Comput. Statist. Data Anal.
    <doi:10.1016/j.csda.2013.02.007> and in Parisi, A., Liseo, B. (2017). Objective Bayesian
    analysis for the multivariate skew-t model. Statistical Methods & Applications
    <doi: 10.1007/s10260-017-0404-0>.
	"""
	
	cran = "mvst" 

	version("1.1.1", md5="617c8510cbabd733306e4a009915f7b1")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
