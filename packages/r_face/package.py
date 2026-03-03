# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFace(RPackage):
	"""Fast Covariance Estimation for Sparse Functional Data

	We implement the Fast Covariance Estimation for 
             Sparse Functional Data paper published in Statistics and Computing <doi: 10.1007/s11222-017-9744-8>.
	"""
	
	cran = "face" 

	version("0.1-7", md5="b98624164f1951299dbccc514c83347f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
