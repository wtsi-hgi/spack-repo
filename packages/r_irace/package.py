# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrace(RPackage):
	"""Iterated Racing for Automatic Algorithm Configuration

	Iterated race is an extension of the Iterated F-race method for
             the automatic configuration of optimization algorithms, that is,
             (offline) tuning their parameters by finding the most appropriate
             settings given a set of instances of an optimization problem.
             M. López-Ibáñez, J. Dubois-Lacoste, L. Pérez Cáceres, T. Stützle,
             and M. Birattari (2016) <doi:10.1016/j.orp.2016.09.002>.
	"""
	
	homepage = "https://mlopez-ibanez.github.io/irace/"
	cran = "irace" 

	version("3.5", md5="a94d91e36f628760e6e32ceac29601f6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
