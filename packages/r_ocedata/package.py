# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcedata(RPackage):
	"""Oceanographic Data Sets for 'oce' Package

	Several Oceanographic data sets are provided for use
    by the 'oce' package and for other purposes.
	"""
	
	homepage = "https://dankelley.github.io/ocedata/"
	cran = "ocedata" 

	version("0.2.2", md5="098aa6a60ec309bc1919326de5430189")

	depends_on("r@3.5:", type=("build", "run"))
