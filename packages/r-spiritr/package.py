# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiritr(RPackage):
	"""Template for Clinical Trial Protocol

	Contains an R Markdown template for a clinical trial 
    protocol adhering to the SPIRIT statement. The SPIRIT (Standard Protocol 
    Items for Interventional Trials) statement outlines recommendations for a 
    minimum set of elements to be addressed in a  clinical trial protocol. 
    Also contains functions to create a xml document from the template and 
    upload it to clinicaltrials.gov<https://www.clinicaltrials.gov/> for 
    trial registration.
	"""
	
	homepage = "https://github.com/awconway/spiritR"
	cran = "spiritR" 

	version("0.1.1", md5="c879f3c142161a6b0f6481007d492d37")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
