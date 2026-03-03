# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirports(RPackage):
	"""Data on Airports

	Geographic, use, and property related data on airports.
	"""
	
	homepage = "https://github.com/OpenIntroStat/airports"
	cran = "airports" 

	version("0.1.0", md5="273c883246a517e92ea38bae4251cae1")

	depends_on("r@2.10:", type=("build", "run"))
