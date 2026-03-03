# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepresent(RPackage):
	"""Determine How Representative Two Multidimensional Data Sets are

	Compute the values of various parameters evaluating how similar two multidimensional datasets' structures are in multidimensional space, as described in: Jouan-Rimbaud, D., Massart, D. L., Saby, C. A., Puel, C. (1998), <doi:10.1016/S0169-7439(98)00005-7>. The computed parameters evaluate three properties, namely, the direction of the data sets, the variance-covariance of the data points, and the location of the data sets' centroids. The package contains workhorse function jrparams(), as well as two helper functions Mboxtest() and JRsMahaldist(), and four example data sets.
	"""
	
	cran = "represent" 

	version("1.0.1", md5="fe1c52db806b468c7d06a87ebffe225b")

