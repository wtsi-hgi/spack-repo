# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointai(RPackage):
	"""Joint Analysis and Imputation of Incomplete Data

	Joint analysis and imputation of incomplete data in the Bayesian
    framework, using (generalized) linear (mixed) models and extensions there of,
    survival models, or joint models for longitudinal and survival data, as
    described in Erler, Rizopoulos and Lesaffre (2021) <doi:10.18637/jss.v100.i20>.
    Incomplete covariates, if present, are automatically imputed.
    The package performs some preprocessing of the data and creates a 'JAGS'
    model, which will then automatically be passed to 'JAGS' 
    <https://mcmc-jags.sourceforge.io/> with the help of 
    the package 'rjags'.
	"""
	
	homepage = "https://nerler.github.io/JointAI/"
	cran = "JointAI" 

	version("1.0.6", md5="27fd54ed903108b3bd4570c47a43298c")
	version("1.0.5", md5="5ab6b8a056689ebdbb07fc542c6fb878")

	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
