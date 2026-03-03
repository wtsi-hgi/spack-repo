# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpfit(RPackage):
	"""Gaussian Processes Modeling

	A computationally stable approach of fitting a Gaussian Process (GP) model to a deterministic simulator. 
	"""
	
	cran = "GPfit" 

	version("1.0-8", md5="1fd122b9f1e19bf6fca7777e59cedd78")

	depends_on("r-lhs@0.5:", type=("build", "run"))
	depends_on("r-lattice@0.18.8:", type=("build", "run"))
