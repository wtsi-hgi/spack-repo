# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRioja(RPackage):
	"""Analysis of Quaternary Science Data

	Constrained clustering, transfer functions, and other methods for analysing Quaternary science data.
	"""
	
	homepage = "http://www.staff.ncl.ac.uk/stephen.juggins/"
	cran = "rioja" 

	version("1.0-6", md5="407e3c07096a26c82a8849db49f1200e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
