# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDonut(RPackage):
	"""Nearest Neighbour Search with Variables on a Torus

	Finds the k nearest neighbours in a dataset of specified points, 
  adding the option to wrap certain variables on a torus.  The user chooses
  the algorithm to use to find the nearest neighbours. Two such algorithms,
  provided by the packages 'RANN' <https://cran.r-project.org/package=RANN>, 
  and 'nabor' <https://cran.r-project.org/package=nabor>, are suggested.
	"""
	
	homepage = "https://github.com/paulnorthrop/donut"
	cran = "donut" 

	version("1.0.3", md5="2dbf01257958df8ab32af2be625b5367")

	depends_on("r@3.3:", type=("build", "run"))
