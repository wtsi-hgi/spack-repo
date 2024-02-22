# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStellar(RPackage):
	"""Evolutionary Tracks and Isochrones from Pisa Stellar Evolution
Database

	Manages and display stellar tracks and isochrones from 
	     Pisa low-mass database. Includes tools for isochrones
	     construction and tracks interpolation. 
	"""
	
	homepage = "The"
	cran = "stellaR" 

	version("0.3-4", md5="d71d23dcedb758843a4ad7b6a912c450")

