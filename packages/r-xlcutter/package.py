# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlcutter(RPackage):
	"""Parse Batches of 'xlsx' Files Based on a Template

	Parse entire folders of non-rectangular 'xlsx' files into a single
  rectangular and tidy 'data.frame' based on a custom template file defining the 
  column names of the output.
	"""
	
	homepage = "https://github.com/Bisaloo/xlcutter"
	cran = "xlcutter" 

	version("0.1.1", md5="e92e4b0bae99d42007bf34ec8c57663d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tidyxl", type=("build", "run"))
