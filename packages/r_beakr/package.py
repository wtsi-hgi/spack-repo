# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeakr(RPackage):
	"""A Minimalist Web Framework for R

	A minimalist web framework for developing application programming 
    interfaces in R that provides a flexible framework for handling common 
    HTTP-requests, errors, logging, and an ability to integrate any R code as 
    server middle-ware.
	"""
	
	homepage = "https://github.com/MazamaScience/beakr"
	cran = "beakr" 

	version("0.4.3", md5="5aebf28a3ca62a22bad87e3d612e7157")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-webutils", type=("build", "run"))
