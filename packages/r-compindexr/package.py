# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompindexr(RPackage):
	"""Calculates Composite Index

	It uses the first-order sensitivity index to measure whether the weights assigned by the creator of the composite indicator match the actual importance of the variables. Moreover, the variance inflation factor is used to reduce the set of correlated variables. In the case of a discrepancy between the importance and the assigned weight, the script determines weights that allow adjustment of the weights to the intended impact of variables. If the optimised weights are unable to reflect the desired importance, the highly correlated variables are reduced, taking into account variance inflation factor. The final outcome of the script is the calculated value of the composite indicator based on optimal weights and a reduced set of variables, and the linear ordering of the analysed objects.
	"""
	
	homepage = "https://github.com/olgnaydn/compindexR"
	cran = "compindexR" 

	version("0.1.3", md5="4f5cbaaecc6a33c65c0e72a5e0fe44f1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-car@3.1:", type=("build", "run"))
	depends_on("r-pracma@2.3.8:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-nlcoptim@0.6:", type=("build", "run"))
