# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCofeaturer(RPackage):
	"""Generate Cofeature Matrices

	Generate cofeature (feature by sample) matrices. The package 
  utilizes ggplot2::geom_tile() to generate the matrix allowing for easy
  additions from the base matrix.
	"""
	
	homepage = "https://github.com/tinyheero/cofeatureR"
	cran = "cofeatureR" 

	version("1.1.1", md5="c8fc2f1c4fd8697f9e277b26de0907ad")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
