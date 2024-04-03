# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixturemissing(RPackage):
	"""Robust and Flexible Model-Based Clustering for Data Sets with
Missing Values at Random

	Implementations of various robust and flexible model-based clustering methods for data sets with missing values at random. 
    Two main models are: Multivariate Contaminated Normal Mixture (MCNM, Tong and Tortora, 2022, <doi:10.1007/s11634-021-00476-1>) and 
    Multivariate Generalized Hyperbolic Mixture (MGHM, Wei et al., 2019, <doi:10.1016/j.csda.2018.08.016>). Mixtures via some special or limiting
    cases of the multivariate generalized hyperbolic distribution are also included: Normal-Inverse Gaussian, Symmetric Normal-Inverse Gaussian, 
    Skew-Cauchy, Cauchy, Skew-t, Student's t, Normal, Symmetric Generalized Hyperbolic, Hyperbolic Univariate Marginals, 
    Hyperbolic, and Symmetric Hyperbolic.
	"""
	
	cran = "MixtureMissing" 

	version("3.0.2", md5="a84d89e5d9dfba9ec66c2be4afb2918c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.2:", type=("build", "run"))
	depends_on("r-mnormt@2.0.2:", type=("build", "run"))
	depends_on("r-cluster@2.1.2:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-numderiv@8.1.1:", type=("build", "run"))
	depends_on("r-bessel@0.6:", type=("build", "run"))
	depends_on("r-mclust@5:", type=("build", "run"))
	depends_on("r-mice@3.10:", type=("build", "run"))
