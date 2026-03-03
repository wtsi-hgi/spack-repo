# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIron(RPackage):
	"""Solving Imbalanced Regression Tasks

	Imbalanced domain learning has almost exclusively focused on solving 
    classification tasks, where the objective is to predict cases labelled with a 
    rare class accurately. Such a well-defined approach for regression tasks lacked 
    due to two main factors. First, standard regression tasks assume that each value 
    is equally important to the user. Second, standard evaluation metrics focus on 
    assessing the performance of the model on the most common cases. This package 
    contains methods to tackle imbalanced domain learning problems in regression 
    tasks, where the objective is to predict extreme (rare) values.
    The methods contained in this package are: 1) an automatic and non-parametric 
    method to obtain such relevance functions; 2) visualisation tools; 3) suite of 
    evaluation measures for optimisation/validation processes; 4) the squared-error 
    relevance area measure, an evaluation metric tailored for imbalanced regression tasks.
    More information can be found in Ribeiro and Moniz (2020) <doi:10.1007/s10994-020-05900-9>.
	"""
	
	homepage = "https://github.com/nunompmoniz/IRon"
	cran = "IRon" 

	version("0.1.4", md5="51b601d7a0dc75ebd3537fb987ba0cad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
