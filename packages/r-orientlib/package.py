# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrientlib(RPackage):
	"""Support for Orientation Data

	Representations, conversions and display of orientation SO(3) data.
 See the orientlib help topic for details.
	"""
	
	homepage = "https://github.com/dmurdoch/orientlib"
	cran = "orientlib" 

	version("0.10.5", md5="622a2c55a665984677aed38135153579")

	depends_on("r@2.13:", type=("build", "run"))
