# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebusDatetimes(RPackage):
	"""Date and Time Extensions for the 'rebus' Package

	Build regular expressions piece by piece using human readable code.
    This package contains date and time functionality, and is primarily intended
    to be used by package developers.
	"""
	
	cran = "rebus.datetimes" 

	version("0.0-2", md5="e9b67009085cfb1ce4bba0a6a3d173b8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rebus-base", type=("build", "run"))
