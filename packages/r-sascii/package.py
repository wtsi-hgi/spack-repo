# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSascii(RPackage):
	"""Import ASCII Files Directly into R using Only a 'SAS' Input
Script

	Using any importation code designed for 'SAS' users to read ASCII files into 'sas7bdat' files, this package parses through the INPUT block of a '.sas' syntax file to design the parameters needed for a 'read.fwf()' function call.  This allows the user to specify the location of the ASCII (often a '.dat') file and the location of the 'SAS' syntax file, and then load the data frame directly into R in just one step.
	"""
	
	homepage = "https://github.com/ajdamico/SAScii"
	cran = "SAScii" 

	version("1.0.2", md5="bf8d9af9a50396485afa2b79ea5e9862")

	depends_on("r@4.2:", type=("build", "run"))
