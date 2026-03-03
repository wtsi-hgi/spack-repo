# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoother(RPackage):
	"""Functions Relating to the Smoothing of Numerical Data

	A collection of methods for smoothing numerical data, commencing
    with a port of the Matlab gaussian window smoothing function. In addition,
    several functions typically used in smoothing of financial data are included.
	"""
	
	cran = "smoother" 

	version("1.3", md5="72d0e18fd958c830eed4db728eb09f5e")
	version("1.1", md5="876f63e324865694589c3ffd1d134d52")

	depends_on("r-ttr@0.22:", type=("build", "run"))
