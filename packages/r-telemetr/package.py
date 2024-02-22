# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTelemetr(RPackage):
	"""Filter and Analyze Generalised Telemetry Data from Organisms

	Analyze telemetry datasets generalized to allow
    any technology. The filtering steps check for false positives caused by 
    reflected transmissions from surfaces and false pings from other noise 
    generating equipment. The filters are based on JSATS filtering algorithms
    found in package 'filteRjsats' <https://CRAN.R-project.org/package=filteRjsats>
    but have been generalized to allow the user to define many of the filtering 
    variables. Additionally, this package contains scripts used to help identify 
    an optimal maximum blanking period as defined in Capello et al (2015) 
    <doi:10.1371/journal.pone.0134002>. The functions were written according to
    their manuscript description, but have not been reviewed by the authors for 
    accuracy. It is included here as is, without warranty.
	"""
	
	cran = "telemetR" 

	version("1.0", md5="9f7297e718907a5354c439a47ae23129")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
