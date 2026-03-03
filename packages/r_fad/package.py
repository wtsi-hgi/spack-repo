# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFad(RPackage):
	"""Factor Analysis for Data

	Compute maximum likelihood estimators of parameters in a Gaussian factor model using
  the the matrix-free methodology described in Dai et al. (2020) <doi:10.1080/10618600.2019.1704296>.
  In contrast to the factanal() function from 'stats' package, fad() can handle high-dimensional datasets where
  number of variables exceed the sample size and is also substantially faster than the EM algorithms.
	"""
	
	homepage = "https://github.com/somakd/fad"
	cran = "fad" 

	version("0.9-1", md5="08ee75f68962713000692e3987d2b3e2")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrix@1.1.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
