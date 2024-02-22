# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfunhddc(RPackage):
	"""Clustering of Functional Data via Mixtures of t-Distributions

	Extension of 'funHDDC' Schmutz et al. (2018) 
    <doi:10.1007/s00180-020-00958-4> for cases including
    outliers by fitting t-distributions for robust groups. 'TFunHDDC' can cluster
    univariate or multivariate data produced by the 'fda' package for data using
    a b-splines or Fourier basis.
	"""
	
	cran = "TFunHDDC" 

	version("1.0.1", md5="ea168791340544933044a40e3cf7a8be")

	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tclust", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
