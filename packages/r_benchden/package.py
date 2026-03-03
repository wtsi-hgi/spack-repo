# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchden(RPackage):
	"""28 Benchmark Densities from Berlinet/Devroye (1994)

	Full implementation of the 28 distributions introduced as benchmarks for nonparametric density estimation by Berlinet and Devroye (1994) <https://hal.science/hal-03659919>. Includes densities, cdfs, quantile functions and generators for samples as well as additional information on features of the densities. Also contains the 4 histogram densities used in Rozenholc/Mildenberger/Gather (2010) <doi:10.1016/j.csda.2010.04.021>. 
	"""
	
	homepage = "https://github.com/thmild/benchden"
	cran = "benchden" 

	version("1.0.8", md5="51a7e22ceb24057b167ec6db0687b81a")

