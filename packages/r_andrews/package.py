# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAndrews(RPackage):
	"""Various Andrews Curves

	Visualisation of multidimensional data through different Andrews curves: 
   Andrews, D. F. (1972) Plots of High-Dimensional Data. Biometrics, 28(1), 125-136. <doi:10.2307/2528964>.
	"""
	
	homepage = "https://github.com/sigbertklinke/andrews"
	cran = "andrews" 

	version("1.1.2", md5="4dc8421a7e733e549235abdd6882ea34")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
