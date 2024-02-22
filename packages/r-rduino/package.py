# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRduino(RPackage):
	"""A Microcontroller Interface

	Functions for connecting to and interfacing with an 'Arduino' or similar device. Functionality includes uploading of sketches, setting and reading digital and analog pins, and rudimentary servo control. This project is not affiliated with the 'Arduino' company, <https://www.arduino.cc/>. 
	"""
	
	cran = "Rduino" 

	version("0.1", md5="ee4bb62c07d7b92d82cf793baa1a4acb")

	depends_on("r-serial", type=("build", "run"))
