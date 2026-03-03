# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckluhn(RPackage):
	"""Checks if a Number is Valid Using the Luhn Algorithm

	Confirms if the number is Luhn compliant.
    Can check if credit card, IMEI number or any other Luhn based number is correct. 
    For more info see: <https://en.wikipedia.org/wiki/Luhn_algorithm>.
	"""
	
	homepage = "https://github.com/adamjdeacon/checkLuhn"
	cran = "checkLuhn" 

	version("1.1.0", md5="acb382d448ddbea3c8f53364816a04e4")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
