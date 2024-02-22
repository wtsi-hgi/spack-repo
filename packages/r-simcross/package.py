# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcross(RPackage):
	"""Simulate Experimental Crosses

	Simulate and plot general experimental crosses. The focus is on simulating genotypes with an aim towards flexibility rather than speed. Meiosis is simulated following the Stahl model, in which chiasma locations are the superposition of two processes: a proportion p coming from a process exhibiting no interference, and the remainder coming from a process following the chi-square model.
	"""
	
	homepage = "https://kbroman.org/simcross/"
	cran = "simcross" 

	version("0.6", md5="b7fcf5537d17732a2cdbab137331a519")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
