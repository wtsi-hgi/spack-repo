# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetassoc(RPackage):
	"""Inference of Species Associations from Co-Occurrence Data

	Infers species associations from community matrices. Uses local and (optional) regional-scale co-occurrence data by comparing observed partial correlation coefficients between species to those estimated from regional species distributions. Extends Gaussian graphical models to a null modeling framework. Provides interface to a variety of inverse covariance matrix estimation methods. 
	"""
	
	cran = "netassoc" 

	version("0.7.0", md5="67ea4b57f036f3381137d928b2f6da49")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
