# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataclean(RPackage):
	"""Data Cleaning

	Includes functions that researchers or practitioners may use to clean
    raw data, transferring html, xlsx, txt data file into other formats. And it
    also can be used to manipulate text variables, extract numeric variables from
    text variables and other variable cleaning processes. It is originated from a
    author's project which focuses on creative performance in online education
    environment. The resulting paper of that study will be published soon.
	"""
	
	cran = "DataClean" 

	version("1.0", md5="f2cf29c8c49417b315a7cf055086bf19")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
