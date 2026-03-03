# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMestim(RPackage):
	"""Computes the Variance-Covariance Matrix of Multidimensional
Parameters Using M-Estimation

	Provides a flexible framework for estimating the variance-covariance matrix of estimated parameters. Estimation relies on unbiased estimating functions to compute the empirical sandwich variance. (i.e., M-estimation in the vein of Tsiatis et al. (2019) <doi:10.1201/9780429192692>.
	"""
	
	cran = "Mestim" 

	version("0.2.1", md5="05bcee06c2bcf202d1fb4ae76a6118b6")

