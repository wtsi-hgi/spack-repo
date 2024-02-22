# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIn2extremes(RPackage):
	"""Into the extRemes Package

	Graphical User Interface (GUI) to some of the functions in the package extRemes version >= 2.0 are included.
	"""
	
	homepage = "http://www.assessment.ucar.edu/toolkit/"
	cran = "in2extRemes" 

	version("1.0-3", md5="62d6ca9912089dd122a31ea9d8ea7a1a")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-extremes@2:", type=("build", "run"))
