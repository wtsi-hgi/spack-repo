# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoronanetr(RPackage):
	"""API Access to 'CoronaNet' Data

	Offers access to a database on government responses to the COVID-19 pandemic. 
    To date, the 'CoronaNet' dataset provides the most comprehensive and granular 
    documentation of such government policies in the world, capturing data for 
    20 broad policy categories alongside many other dimensions, including the 
    initiator, target, and timing of a policy. This package is a programmatic 
    front-end to up-to-date 'CoronaNet' policy records and the 'CoronaNet' policy intensity index scores. 
    For more information, see Cheng et al. (2020) <doi:10.1038/s41562-020-0909-7>.
	"""
	
	homepage = "https://github.com/CoronaNetDataScience/CoronaNetR"
	cran = "CoronaNetR" 

	version("0.3.0", md5="d4a4510dc627f9b75d91affe22f62e89")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
