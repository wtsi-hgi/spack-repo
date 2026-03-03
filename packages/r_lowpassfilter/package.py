# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowpassfilter(RPackage):
	"""Lowpass Filtering

	Creates lowpass filters which are commonly used in ion channel recordings. It supports generation of random numbers that are filtered, i.e. follow a model for ion channel recordings, see <doi:10.1109/TNB.2018.2845126>. Furthermore, time continuous convolutions of piecewise constant signals with the kernel of lowpass filters can be computed.
	"""
	
	cran = "lowpassFilter" 

	version("1.0-2", md5="69df80a755777bfa485b4212ec8c11ae")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
