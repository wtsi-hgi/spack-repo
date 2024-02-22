# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThermocouple(RPackage):
	"""Temperature Measurement with Thermocouples, RTD and IC Sensors

	Temperature measurement data, equations and methods for thermocouples,
    wire RTD, thermistors, IC thermometers, bimetallic strips and the ITS-90.
	"""
	
	cran = "thermocouple" 

	version("1.0.2", md5="5270c114627a52b779bf5b7620ae81aa")

	depends_on("r@2.7:", type=("build", "run"))
