# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmpichar(RPackage):
	"""Evaluates the Empirical Characteristic Function for Multivariate
Samples

	Evaluates the empirical characteristic function of univariate and multivariate samples.
    This package uses 'RcppArmadillo' for fast evaluation. It is also possible to export the code to be used in other packages at 'C++' level.
	"""
	
	homepage = "https://github.com/gbasulto/empichar"
	cran = "empichar" 

	version("1.0.1", md5="6215c32be59477d64142bfd059e650b1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
