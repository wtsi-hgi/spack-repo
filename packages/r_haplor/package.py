# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaplor(RPackage):
	"""Query 'HaploReg', 'RegulomeDB'

	A set of utilities for querying 
             'HaploReg' <https://pubs.broadinstitute.org/mammals/haploreg/haploreg.php>, 
             'RegulomeDB' <https://www.regulomedb.org/regulome-search/> 
             web-based tools. The package connects to 
             'HaploReg', 'RegulomeDB' searches and downloads results, without 
             opening web pages, directly from R environment. 
             Results are stored in a data frame that can be directly used in various 
             kinds of downstream analyses.
	"""
	
	cran = "haploR" 

	version("4.0.7", md5="2a139873bfb0351197640fbf64ef41cb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
