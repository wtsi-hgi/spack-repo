# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutohrf(RPackage):
	"""Automated Generation of Data-Informed GLM Models in Task-Based
fMRI Data Analysis

	Analysis of task-related functional magnetic resonance imaging (fMRI) activity at the level of individual participants is commonly based on general linear modelling (GLM) that allows us to estimate to what extent the blood oxygenation level dependent (BOLD) signal can be explained by task response predictors specified in the GLM model. The predictors are constructed by convolving the hypothesised timecourse of neural activity with an assumed hemodynamic response function (HRF). To get valid and precise estimates of task response, it is important to construct a model of neural activity that best matches actual neuronal activity. The construction of models is most often driven by predefined assumptions on the components of brain activity and their duration based on the task design and specific aims of the study. However, our assumptions about the onset and duration of component processes might be wrong and can also differ across brain regions. This can result in inappropriate or suboptimal models, bad fitting of the model to the actual data and invalid estimations of brain activity. Here we present an approach in which theoretically driven models of task response are used to define constraints based on which the final model is derived computationally using the actual data. Specifically, we developed 'autohrf' — a package for the 'R' programming language that allows for data-driven estimation of HRF models. The package uses genetic algorithms to efficiently search for models that fit the underlying data well. The package uses automated parameter search to find the onset and duration of task predictors which result in the highest fitness of the resulting GLM based on the fMRI signal under predefined restrictions. We evaluate the usefulness of the 'autohrf' package on publicly available datasets of task-related fMRI activity. Our results suggest that by using 'autohrf' users can find better task related brain activity models in a quick and efficient manner.
	"""
	
	homepage = "https://github.com/demsarjure/autohrf"
	cran = "autohrf" 

	version("1.1.3", md5="24d147d97141ad60ffd1bcf53ce227d7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot@1.1.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-gtools@3.9.2:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-magrittr@2.0.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
