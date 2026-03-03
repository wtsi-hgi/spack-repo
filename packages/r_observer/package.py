# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObserver(RPackage):
	"""Observe and Check your Data

	Checks that a given dataset passes user-specified 
    rules. The main functions are observe_if() and inspect(). 
	"""
	
	homepage = "https://github.com/paulponcet/observer"
	cran = "observer" 

	version("0.1.2", md5="dfd76a9c7f9cf16ae28fa41f214cef13")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-bazar", type=("build", "run"))
	depends_on("r-bit", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
