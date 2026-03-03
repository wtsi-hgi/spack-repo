# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnviewer(RPackage):
	"""Bayesian Networks Interactive Visualization and Explainable
Artificial Intelligence

	Bayesian networks provide an intuitive framework for probabilistic reasoning 
             and its graphical nature can be interpreted quite clearly. Graph based methods 
             of machine learning are becoming more popular because they offer a richer model 
             of knowledge that can be understood by a human in a graphical format. The 'bnviewer' 
             is an R Package that allows the interactive visualization of Bayesian Networks. 
             The aim of this package is to improve the Bayesian Networks visualization over 
             the basic and static views offered by existing packages.
	"""
	
	homepage = "http://robsonfernandes.net/bnviewer/"
	cran = "bnviewer" 

	version("0.1.6", md5="5b90aba2b11c8b990f49576af6d46dbb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-visnetwork@2.0.4:", type=("build", "run"))
	depends_on("r-bnlearn@4.3:", type=("build", "run"))
	depends_on("r-igraph@1.2.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
