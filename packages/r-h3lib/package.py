# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH3lib(RPackage):
	"""Exposes the 'Uber' 'H3' Library to R Packages

	'H3' is a hexagonal hierarchical spatial index developed by 'Uber' <https://h3geo.org/>.
  This package exposes the source code of 'H3' (written in 'C') to routines that are callable through 'R'.
	"""
	
	homepage = "https://github.com/symbolixau/h3lib"
	cran = "h3lib" 

	version("0.1.3", md5="30ff8ba6b4ac4e5d7496d954eb354f9b")

	depends_on("r@3:", type=("build", "run"))
