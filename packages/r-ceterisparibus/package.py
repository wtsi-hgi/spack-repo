# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeterisparibus(RPackage):
	"""Ceteris Paribus Profiles

	Ceteris Paribus Profiles (What-If Plots) are designed to present model 
    responses around selected points in a feature space. 
    For example around a single prediction for an interesting observation. 
    Plots are designed to work in a model-agnostic fashion, they are working 
    for any predictive Machine Learning model and allow for model comparisons.
    Ceteris Paribus Plots supplement the Break Down Plots from 'breakDown' package.
	"""
	
	homepage = "https://pbiecek.github.io/ceterisParibus/"
	cran = "ceterisParibus" 

	version("0.4.2", md5="d3583351ae3c51948e0c08d0b08f7280")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
