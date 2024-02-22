# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIemiscdata(RPackage):
	"""Irucka Embry's Miscellaneous Data Collection

	Miscellaneous data sets [Chemistry, Engineering Economics,
    Environmental/Water Resources Engineering, Nuclear Accidents, US
    Presidential Elections, and US Continental Congress Presidents].
	"""
	
	homepage = "https://gitlab.com/iembry/iemiscdata"
	cran = "iemiscdata" 

	version("1.0.1", md5="ccaa4fbcdcd715f5a7a9cccb3b3f520c")

	depends_on("r@3.5:", type=("build", "run"))
