# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorset(RPackage):
	"""Arbitrary Bounding of Series and Time Series Objects

	Set of methods to constrain numerical series and time series within
             arbitrary boundaries.
	"""
	
	cran = "corset" 

	version("0.1-5", md5="574072f620198abbb13337decaf15a1e")

	depends_on("r@2.10:", type=("build", "run"))
