# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalmodel(RPackage):
	"""LIME-Based Explanations with Interpretable Inputs Based on
Ceteris Paribus Profiles

	Local explanations of machine learning models describe, how features contributed to a single prediction. 
    This package implements an explanation method based on LIME 
    (Local Interpretable Model-agnostic Explanations, 
    see Tulio Ribeiro, Singh, Guestrin (2016) <doi:10.1145/2939672.2939778>) in which interpretable
    inputs are created based on local rather than global behaviour of each original feature.
	"""
	
	homepage = "https://github.com/ModelOriented/localModel"
	cran = "localModel" 

	version("0.5", md5="3aaf66393774091245cec7e6a397ff61")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-ingredients", type=("build", "run"))
