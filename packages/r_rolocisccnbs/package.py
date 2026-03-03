# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolocisccnbs(RPackage):
	"""A Colour List and Colour Metric Based on the ISCC-NBS System of
Color Designation

	A colour list and colour metric based on the ISCC-NBS System of Color Designation for use with the 'roloc' package for converting colour specifications to colour names.
	"""
	
	cran = "rolocISCCNBS" 

	version("0.1", md5="3dcf90fea0f573de385581b1a9c38ec4")

	depends_on("r-roloc", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
