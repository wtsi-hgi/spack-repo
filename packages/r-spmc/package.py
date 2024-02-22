# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpmc(RPackage):
	"""Continuous-Lag Spatial Markov Chains

	A set of functions is provided for 1) the stratum lengths analysis along a chosen direction, 2) fast estimation of continuous lag spatial Markov chains model parameters and probability computing (also for large data sets), 3) transition probability maps and transiograms drawing, 4) simulation methods for categorical random fields. More details on the methodology are discussed in Sartore (2013) <doi:10.32614/RJ-2013-022> and Sartore et al. (2016) <doi:10.1016/j.cageo.2016.06.001>.
	"""
	
	cran = "spMC" 

	version("0.3.15", md5="6f46d80ab31c442ba5459f1256f0ab2d")

	depends_on("r@3:", type=("build", "run"))
