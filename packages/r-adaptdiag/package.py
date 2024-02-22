# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptdiag(RPackage):
	"""Bayesian Adaptive Designs for Diagnostic Trials

	Simulate clinical trials for diagnostic test devices and evaluate 
    the operating characteristics under an adaptive design with futility
    assessment determined via the posterior predictive probabilities.
	"""
	
	homepage = "https://github.com/graemeleehickey/adaptDiag"
	cran = "adaptDiag" 

	version("0.1.0", md5="97807d2b984be71684e42c4f20670013")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
