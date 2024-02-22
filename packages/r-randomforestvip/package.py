# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomforestvip(RPackage):
	"""Tune Random Forests Based on Variable Importance & Plot Results

	Functions for assessing variable relations and associations 
    prior to modeling with a Random Forest algorithm (although these are 
    relevant for any predictive model).
    Metrics such as partial correlations and variance inflation factors
    are tabulated as well as plotted for the user. A function is available
    for tuning the main Random Forest hyper-parameter based on model performance 
    and variable importance metrics. This grid-search technique provides
    tables and plots showing the effect of the main hyper-parameter on each 
    of the assessment metrics. It also returns each of the evaluated models 
    to the user. The package also provides superior variable importance plots 
    for individual models. All of the plots are developed so that the 
    user has the ability to edit and improve further upon the 
    plots. Derivations and methodology are described in Bladen (2022) 
    <https://digitalcommons.usu.edu/etd/8587/>.
	"""
	
	homepage = "https://github.com/KelvynBladen/randomForestVIP"
	cran = "randomForestVIP" 

	version("0.1.3", md5="69e1fdefb23b3b164bf79e1116e4bced")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
