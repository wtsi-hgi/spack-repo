# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomPolychorPa(RPackage):
	"""A Parallel Analysis with Polychoric Correlation Matrices

	The Function performs a parallel analysis using simulated polychoric correlation matrices. The nth-percentile of the eigenvalues distribution obtained from both the randomly generated and the real data polychoric correlation matrices is returned. A plot comparing the two types of eigenvalues (real and simulated) will help determine the number of real eigenvalues that outperform random data. The function is based on the idea that if real data are non-normal and the polychoric correlation matrix is needed to perform a Factor Analysis, then the Parallel Analysis method used to choose a non-random number of factors should also be based on randomly generated polychoric correlation matrices and not on Pearson correlation matrices. Random data sets are simulated assuming or a uniform or a multinomial distribution or via the bootstrap method of resampling (i.e., random permutations of cases). Also Multigroup Parallel analysis is made available for random (uniform and multinomial distribution and with or without difficulty factor) and bootstrap methods. An option to choose between default or full output is also available as well as a parameter to print Fit Statistics (Chi-squared, TLI, RMSEA, RMR and BIC) for the factor solutions indicated by the Parallel Analysis. Also weighted correlation matrices may be considered for PA. 
	"""
	
	cran = "random.polychor.pa" 

	version("1.1.4-5", md5="81795f8343b0c4fc5d44e4d17247de9c")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-nfactors", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
