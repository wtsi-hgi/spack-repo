# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegda(RPackage):
	"""Regularised Discriminant Analysis

	Regularised discriminant analysis functions. The classical regularised discriminant analysis proposed by Friedman in 1989, including cross-validation, of which the linear and quadratic discriminant analyses are special cases. Further, the regularised maximum likelihood linear discriminant analysis, including cross-validation. References: Friedman J.H. (1989): "Regularized Discriminant Analysis". Journal of the American Statistical Association 84(405): 165--175. <doi:10.2307/2289860>. Friedman J., Hastie T. and Tibshirani R. (2009). "The elements of statistical learning", 2nd edition. Springer, Berlin. <doi:10.1007/978-0-387-84858-7>. Tsagris M., Preston S. and Wood A.T.A. (2016). "Improved classification for compositional data using the alpha-transformation". Journal of Classification, 33(2): 243--261. <doi:10.1007/s00357-016-9207-5>.
	"""
	
	cran = "regda" 

	version("1.0", md5="0a05ece3491703801746d17a7fd2a723")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
