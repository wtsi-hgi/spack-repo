# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixlda(RPackage):
	"""Penalized Matrix-Normal Linear Discriminant Analysis

	Fits the penalized matrix-normal model to be used for linear discriminant analysis with matrix-valued predictors. For a description of the method, see Molstad and Rothman (2018) <doi:10.1080/10618600.2018.1476249>. 
	"""
	
	homepage = "ajmolstad@github.io"
	cran = "MatrixLDA" 

	version("0.2", md5="6f6adc4cd3c25e1cb769d9a036f92fe3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
