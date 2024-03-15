# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcheology(RPackage):
	"""Data on Base and Recommended Packages for Current and Previous
Versions of R

	Provides a dataset of functions in all base and recommended packages of R versions 0.50 onwards.
	"""
	
	homepage = "https://github.com/hughjonesd/rcheology"
	cran = "rcheology" 

	version("4.3.3.0", md5="a1a985ec18bfa22ca863a657790a0af1")

	depends_on("r@2.10:", type=("build", "run"))
