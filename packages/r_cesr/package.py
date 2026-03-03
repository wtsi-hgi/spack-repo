# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCesr(RPackage):
	"""Access the Canadian Election Study Datasets

	Makes accessing and loading the Canadian Election Study (<http://www.ces-eec.ca/>, <https://ces-eec.arts.ubc.ca/>, <https://search1.odesi.ca/#/>) surveys into the R workspace more efficient by 
  downloading a requested survey and loading it as a data object. This removes the need to locate, download, load, 
  and change working directories when working with the Canadian Election Study surveys.
	"""
	
	homepage = "https://hodgettsp.github.io/cesR/"
	cran = "cesR" 

	version("0.1.0", md5="55332f10ea5b5ef6179c1ea41a6a272d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
