# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaiser(RPackage):
	"""Comparison of Algorithms with Iterative Sample Size Estimation

	Functions for performing experimental comparisons of algorithms 
             using adequate sample sizes for power and accuracy. Implements the 
             methodology originally presented in Campelo and Takahashi (2019) 
             <doi:10.1007/s10732-018-9396-7> 
             for the comparison of two algorithms, and later generalised in 
             Campelo and Wanner (Submitted, 2019) <arxiv:1908.01720>.
	"""
	
	homepage = "https://fcampelo.github.io/CAISEr/"
	cran = "CAISEr" 

	version("1.0.17", md5="bf581f8dd09eff8b29a5892f065c490e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-pbmcapply@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
