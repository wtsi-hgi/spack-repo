# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSalty(RPackage):
	"""Turn Clean Data into Messy Data

	Take real or simulated data and salt it with errors commonly 
    found in the wild, such as pseudo-OCR errors, Unicode problems, numeric 
    fields with nonsensical punctuation, bad dates, etc.
	"""
	
	homepage = "https://github.com/mdlincoln/salty"
	cran = "salty" 

	version("0.1.0", md5="d64591ee4e3ef8585d1de03b010bfa03")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
