# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumkm(RPackage):
	"""Create a Kaplan-Meier Plot with Numbers at Risk

	To add the table of numbers at risk below the Kaplan-Meier plot.
	"""
	
	cran = "numKM" 

	version("0.2.0", md5="4b7e308991416a3a3b1152791d1216cc")

	depends_on("r-survival", type=("build", "run"))
