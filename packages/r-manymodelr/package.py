# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManymodelr(RPackage):
	"""Build and Tune Several Models

	Frequently one needs a convenient way to build and tune
             several models in one go.The goal is to provide a number of machine learning convenience 
             functions. It provides the ability to build, tune and obtain predictions of 
             several models in one function. The models are built using functions from
             'caret' with easier to read syntax.
             Kuhn(2014) <arXiv:1405.6974>.
	"""
	
	homepage = "https://github.com/Nelson-Gon/manymodelr"
	cran = "manymodelr" 

	version("0.3.7", md5="25868584ff2b957e1f15cf70e7f64369")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-caret@6.0.88:", type=("build", "run"))
	depends_on("r-metrics@0.1.4:", type=("build", "run"))
	depends_on("r-e1071@1.7.8:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-lme4@1.1.27.1:", type=("build", "run"))
