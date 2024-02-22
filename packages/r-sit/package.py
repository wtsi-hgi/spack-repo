# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSit(RPackage):
	"""Association Measurement Through Sliced Independence Test (SIT)

	Computes the sit coefficient between two vectors x and y, 
  possibly all paired coefficients for a matrix. The reference for the methods implemented here is 
  Zhang, Yilin, Canyi Chen, and Liping Zhu. 2022. "Sliced Independence Test." Statistica Sinica. <doi:10.5705/ss.202021.0203>. 
  This package incorporates the Galton peas example.
	"""
	
	cran = "SIT" 

	version("0.1.0", md5="226457af28bca056d53a9e3b3a050fa9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
