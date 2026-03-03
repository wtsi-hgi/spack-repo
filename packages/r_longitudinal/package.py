# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongitudinal(RPackage):
	"""Analysis of Multiple Time Course Data

	Contains general data structures and
  functions for longitudinal data with multiple variables, 
  repeated measurements, and irregularly spaced time points.
  Also implements a shrinkage estimator of dynamical correlation
  and dynamical covariance.
	"""
	
	homepage = "https://strimmerlab.github.io/software/longitudinal/"
	cran = "longitudinal" 

	version("1.1.13", md5="ac7842e3fa9e4f5a5a1ce49c66a20317")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
