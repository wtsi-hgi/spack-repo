# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcesearch(RPackage):
	"""'ACE' Search Engine API

	'ACE' (Advanced Cohort Engine) is a powerful tool that allows constructing cohorts of patients 
             extremely quickly and efficiently. This package is designed to interface directly with an 
             instance of 'ACE' search engine and facilitates API queries and data dumps. Prerequisite
             is a good knowledge of the temporal language to be able to efficiently construct a query.
             More information available at <https://shahlab.stanford.edu/start>.
	"""
	
	homepage = "https://shahlab.stanford.edu/start"
	cran = "ACEsearch" 

	version("1.0.0", md5="efca4f237f0b89e4f3544f7f7ab101d5")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
