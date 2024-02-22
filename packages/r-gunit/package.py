# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGunit(RPackage):
	"""Converts Conductance Units

	For plant physiologists, converts conductance (e.g. stomatal conductance) to different units: m/s, mol/m^2/s, and umol/m^2/s/Pa.
	"""
	
	homepage = "https://github.com/cdmuir/gunit"
	cran = "gunit" 

	version("1.0.2", md5="0ae96146fff13f4bdcedb45e21a680e5")

	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-units@0.6:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
