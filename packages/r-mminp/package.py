# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMminp(RPackage):
	"""Microbe-Metabolite Interactions-Based Metabolic Profiles
Predictor

	
     Implements a computational framework to predict microbial community-based 
     metabolic profiles with 'O2PLS' model. It provides procedures of model 
     training and prediction. Paired microbiome and metabolome data are needed 
     for modeling, and the trained model can be applied to predict metabolites 
     of analogous environments using new microbial feature abundances.
	"""
	
	homepage = "https://github.com/YuLab-SMU/MMINP"
	cran = "MMINP" 

	version("0.1.0", md5="0db6d14333fdd9db328503167b706847")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-omicspls@2.0.2:", type=("build", "run"))
