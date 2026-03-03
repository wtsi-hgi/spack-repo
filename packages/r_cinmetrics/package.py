# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCinmetrics(RPackage):
	"""Calculate Chromosomal Instability Metrics

	Implement various chromosomal instability metrics. 'CINmetrics' (Chromosomal INstability metrics) provides functions to 
    calculate various chromosomal instability metrics on masked Copy Number Variation(CNV) data at individual sample level. The 
    chromosomal instability metrics have been implemented as described in the following studies: 
    Baumbusch LO et al. 2013 <doi:10.1371/journal.pone.0054356>, 
    Davidson JM et al. 2014 <doi:10.1371/journal.pone.0079079>, 
    Chin SF et al. 2007 <doi:10.1186/gb-2007-8-10-r215>.
	"""
	
	cran = "CINmetrics" 

	version("0.1.0", md5="bd1cf0535bb22ea59e0305d7b9647d2e")

	depends_on("r@2.10:", type=("build", "run"))
