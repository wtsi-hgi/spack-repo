# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGents(RPackage):
	"""R Shiny App for Creating Simplified Trial Summary (TS) Domain

	Make it easy to create simplified trial summary (TS) domain
  based on FDA FDA guide
  <https://github.com/TuCai/phuse/blob/master/inst/examples/07_genTS/www/Simplified_TS_Creation_Guide_v2.pdf>.
	"""
	
	cran = "genTS" 

	version("0.1.4", md5="b59345370cce37059373f55742d7b84a")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
