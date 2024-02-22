# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcamatchr(RPackage):
	"""Match Cases to Controls Based on Genotype Principal Components

	Matches cases to controls based on genotype principal components (PC). 
      In order to produce better results, matches are based on the weighted 
      distance of PCs where the weights are equal to the % variance explained 
      by that PC. A weighted Mahalanobis distance metric (Kidd et al. (1987)
      <DOI:10.1016/0031-3203(87)90066-5>) is used to determine matches. 
	"""
	
	homepage = "https://github.com/machiela-lab/PCAmatchR"
	cran = "PCAmatchR" 

	version("0.3.3", md5="0725673f850d4407b99f10b9eaf1bb71")

	depends_on("r@3.5:", type=("build", "run"))
