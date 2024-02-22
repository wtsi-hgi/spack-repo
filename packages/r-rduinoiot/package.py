# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRduinoiot(RPackage):
	"""'Arduino Iot Cloud API' R Client

	Easily interact with the 'Arduino Iot Cloud API' <https://www.arduino.cc/reference/en/iot/api/>, managing devices, things, properties and data.
	"""
	
	homepage = "https://flavioleccese92.github.io/Rduinoiot/"
	cran = "Rduinoiot" 

	version("0.1.0", md5="159c7355f05c723bcb39f11c400ec5f0")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
