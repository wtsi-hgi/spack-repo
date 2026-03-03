# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedicare(RPackage):
	"""Tools for Obtaining and Cleaning Medicare Public Use Files

	Publicly available data from Medicare frequently requires extensive
    initial effort to extract desired variables and merge them; this package
    formalizes the techniques I've found work best. More information on the 
    Medicare program, as well as guidance for the publicly available data this package 
    targets, can be found on CMS's website covering publicly available data. See <https://www.cms.gov/Research-Statistics-Data-and-Systems/Research-Statistics-Data-and-Systems.html>.
	"""
	
	homepage = "http://www.github.com/robertgambrel/medicare"
	cran = "medicare" 

	version("0.2.1", md5="947c674614cb47477786a89162c849d8")

	depends_on("r@2.10:", type=("build", "run"))
