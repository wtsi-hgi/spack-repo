# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfcolours(RPackage):
	"""Government Analysis Function Recommended Accessible Colour
Palette

	Government Analysis Function recommended colours for use in
    charts on gov.uk to help meet accessibility guidance.
	"""
	
	cran = "afcolours" 

	version("1.0.0", md5="88a38b36c0b8668ec072ca6a2c7ef876")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
