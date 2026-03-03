# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrapezoid(RPackage):
	"""The Trapezoidal Distribution

	The trapezoid package provides 'dtrapezoid', 'ptrapezoid', 'qtrapezoid',
    and 'rtrapezoid' functions for the trapezoidal distribution.
	"""
	
	cran = "trapezoid" 

	version("2.0-2", md5="9a30f8397f082865209a3b8e5e6d717a")

	depends_on("r@2.12:", type=("build", "run"))
