# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssAdd(RPackage):
	"""Extra Additive Terms for Generalized Additive Models for
Location Scale and Shape

	Interface for extra smooth functions including tensor products, 
             neural networks and decision trees.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.add" 

	version("5.1-12", md5="6b4c6a53c9dc83824fe72699980e1c48")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss@2.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
