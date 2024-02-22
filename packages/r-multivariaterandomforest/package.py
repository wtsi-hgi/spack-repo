# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivariaterandomforest(RPackage):
	"""Models Multivariate Cases Using Random Forests

	Models and predicts multiple output features in single random forest considering the 
    linear relation among the output features, see details in Rahman et al (2017)<doi:10.1093/bioinformatics/btw765>.
	"""
	
	cran = "MultivariateRandomForest" 

	version("1.1.5", md5="003a999746d87c39c57d1d6a22692735")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
