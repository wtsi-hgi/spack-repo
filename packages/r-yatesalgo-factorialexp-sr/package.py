# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYatesalgoFactorialexpSr(RPackage):
	"""Yates' Algorithm in 2^n Factorial Experiment

	Determines the sum of squares of the (2^n)-1 factorial effects in a 2^n factorial experiment using Yates' algorithm.
	"""
	
	cran = "YatesAlgo.FactorialExp.SR" 

	version("4.0.4", md5="dbd4a3ea824ab835cf43c273c395c1bf")

	depends_on("r-lubridate", type=("build", "run"))
