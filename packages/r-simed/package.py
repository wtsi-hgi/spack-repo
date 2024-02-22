# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimed(RPackage):
	"""Simulation Education

	Contains various functions to be used for simulation education,
    including simple Monte Carlo simulation functions, queueing simulation
    functions, variate generation functions capable of producing independent
    streams and antithetic variates, functions for illustrating random variate
    generation for various discrete and continuous distributions, and functions
    to compute time-persistent statistics.  Also contains functions for 
    visualizing: event-driven details of a single-server queue model; a Lehmer
    random number generator; variate generation via acceptance-rejection; and
    of generating a non-homogeneous Poisson process via thinning.  Also
    contains two queueing data sets (one fabricated, one real-world) to
    facilitate input modeling.  More details on the use of these functions can
    be found in Lawson and Leemis (2015) <doi:10.1109/WSC.2017.8248124>, in
    Kudlay, Lawson, and Leemis (2020) <doi:10.1109/WSC48552.2020.9384010>, and
    in Lawson and Leemis (2021) <doi:10.1109/WSC52266.2021.9715299>.
	"""
	
	cran = "simEd" 

	version("2.0.1", md5="31038cec450ff203dcccf6fc97cde52a")

	depends_on("r-rstream", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
