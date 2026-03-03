# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD4talinkLight(RPackage):
	"""FAIR Data - Workflow Management

	Tools, methods and processes for the management 
  of analysis workflows. These lightweight solutions facilitate 
  structuring R&D activities. These solutions were developed to comply with FAIR 
  principles as discussed by Jacobsen et al. (2017) <doi:10.1162/dint_r_00024>, 
  and with ALCOA+ principles as proposed by the U.S. FDA. 
	"""
	
	homepage = "https://bitbucket.org/SQ4/d4talink.light"
	cran = "D4TAlink.light" 

	version("2.1.14", md5="033a8f4f2d4862a5ae8e19d3b956aec1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
