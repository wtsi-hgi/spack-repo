# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingr(RPackage):
	"""Simultaneous Non-Gaussian Component Analysis

	Implementation of SING algorithm to extract joint and individual non-Gaussian components from two datasets. SING uses an objective function that maximizes the skewness and kurtosis of latent components with a penalty to enhance the similarity between subject scores. Unlike other existing methods, SING does not use PCA for dimension reduction, but rather uses non-Gaussianity, which can improve feature extraction. Benjamin B.Risk, Irina Gaynanova (2021) <doi:10.1214/21-AOAS1466>.  
	"""
	
	cran = "singR" 

	version("0.1.2", md5="ae55bab203008121b3029e5f0438546b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass@7.3.57:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-clue@0.3.61:", type=("build", "run"))
	depends_on("r-gam@1.20.1:", type=("build", "run"))
	depends_on("r-ictest@0.3.5:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
