# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegrsm(RPackage):
	"""Random Subspace Method (RSM) for Linear Regression

	Performs Random Subspace Method (RSM) for high-dimensional linear regression to obtain variable importance measures. The final model is chosen based on validation set or Generalized Information Criterion.
	"""
	
	homepage = "http://www.ipipan.eu/~teisseyrep/SOFTWARE/"
	cran = "regRSM" 

	version("0.5", md5="0fce0eae61e71dcd9e9134d14eacc2f0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmpi", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
