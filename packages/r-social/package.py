# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocial(RPackage):
	"""Social Autocorrelation

	A set of functions to quantify and visualise 
    social autocorrelation.
	"""
	
	cran = "social" 

	version("1.0", md5="7660ba7c1515d57a4ee0c32633fc7c16")

	depends_on("r-rcpp", type=("build", "run"))
