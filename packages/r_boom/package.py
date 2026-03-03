# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoom(RPackage):
	"""Bayesian Object Oriented Modeling

	A C++ library for Bayesian modeling, with an emphasis on Markov
   chain Monte Carlo.  Although boom contains a few R utilities (mainly plotting
   functions), its primary purpose is to install the BOOM C++ library on your
   system so that other packages can link against it.
	"""
	
	cran = "Boom" 

	version("0.9.15", md5="4a0c497336570708c98b611676359249")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
