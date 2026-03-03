# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsbayes(RPackage):
	"""Bayesian Subgroup Analysis in Clinical Trials

	Calculate posterior modes and credible intervals of parameters of the Dixon-Simon model for subgroup analysis (with binary covariates) in clinical trials. For details of the methodology, please refer to D.O. Dixon and R. Simon (1991), Biometrics, 47: 871-881.
	"""
	
	cran = "DSBayes" 

	version("2023.1.0", md5="8828a0137610e5b5d32b05e761a55311")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
