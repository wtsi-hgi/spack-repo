# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacesrgb(RPackage):
	"""Standard and User-Defined RGB Color Spaces, with Conversion
Between RGB and CIE XYZ

	Standard RGB spaces included are sRGB, 'Adobe' RGB, 'ProPhoto' RGB, BT.709, and others.  User-defined RGB spaces are also possible.  There is partial support for ACES Color workflows.
	"""
	
	cran = "spacesRGB" 

	version("1.5-0", md5="f7e126322e0bef2ec780f6d9ca757def")

	depends_on("r@2.13:", type=("build", "run"))
