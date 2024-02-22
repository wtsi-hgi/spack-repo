# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVindecodr(RPackage):
	"""Provides an Interface to the Department of Transportation VIN
Decoder

	Provides a programmatic interface in R for the US Department of 
    Transportation (DOT) National Highway Transportation Safety Administration 
    (NHTSA) vehicle identification number (VIN) API, located at 
    <https://vpic.nhtsa.dot.gov/api/>. 
    The API can decode up to 50 vehicle identification numbers in one call, and 
    provides manufacturer information about the vehicles, including make, model, 
    model year, and gross vehicle weight rating (GVWR).
	"""
	
	cran = "vindecodr" 

	version("0.1.1", md5="ede0091838f5a41f78a19e11a8e1defb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
