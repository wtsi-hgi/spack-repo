# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeppm(RPackage):
	"""Piecewise Exponential Distribution with Random Time Grids

	Fits the Piecewise Exponential distribution with random time grids using the clustering structure of the Product Partition Models. Details of the implemented model can be found in Demarqui et al. (2008) <doi:10.1007/s10985-008-9086-0>.
	"""
	
	homepage = "https://github.com/fndemarqui/peppm"
	cran = "peppm" 

	version("0.0.1", md5="35f5f4570c353e94d18b906a7a12946e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
