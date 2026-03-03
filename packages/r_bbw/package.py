# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbw(RPackage):
	"""Blocked Weighted Bootstrap

	The blocked weighted bootstrap (BBW) is an estimation technique 
    for use with data from two-stage cluster sampled surveys in which either 
    prior weighting (e.g. population-proportional sampling or PPS as used in 
    Standardized Monitoring and Assessment of Relief and Transitions or SMART 
    surveys) or posterior weighting (e.g. as used in rapid assessment method or
    RAM and simple spatial sampling method or S3M surveys) is implemented. See 
    Cameron et al (2008) <doi:10.1162/rest.90.3.414> for application of 
    bootstrap to cluster samples. See Aaron et al (2016) 
    <doi:10.1371/journal.pone.0163176> and Aaron et al (2016) 
    <doi:10.1371/journal.pone.0162462> for application of the blocked weighted 
    bootstrap to estimate indicators from two-stage cluster sampled surveys.
	"""
	
	homepage = "https://github.com/rapidsurveys/bbw"
	cran = "bbw" 

	version("0.2.0", md5="cd61930354ab7ce807574f63b846af81")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
