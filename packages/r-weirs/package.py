# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeirs(RPackage):
	"""A Hydraulics Package to Compute Open-Channel Flow over Weirs

	Provides computational support for flow over weirs, such as sharp-crested, broad-crested, and embankments. Initially, the package supports broad- and sharp-crested weirs.
	"""
	
	cran = "weirs" 

	version("0.25", md5="44f66d91d8d561601b279c2c3fafedf6")

	depends_on("r@2.7:", type=("build", "run"))
