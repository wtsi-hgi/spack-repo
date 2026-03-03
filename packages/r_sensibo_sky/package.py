# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensiboSky(RPackage):
	"""Access to 'Sensibo Sky' API V2 for Air Conditioners Remote
Control

	Provides an interface to the 'Sensibo Sky' API which allows to remotely control non-smart air conditioning units.
  See <https://sensibo.com> for more informations.
	"""
	
	homepage = "https://github.com/theclue/sensibo.sky"
	cran = "sensibo.sky" 

	version("1.0.0", md5="ea88332d035d35ce7656efe7cdeaf940")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
