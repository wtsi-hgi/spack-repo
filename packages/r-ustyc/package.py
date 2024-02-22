# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUstyc(RPackage):
	"""Fetch US Treasury yield curve data

	Forms a query to submit for US Treasury yield curve data, posting
    this query to the US Treasury web site's data feed service.  By default the
    download includes data yield data for 12 products from January 1, 1990,
    some of which are NA during this span.  The caller can pass parameters to
    limit the query to a certain year or year and month, but the full download
    is not especially large.  The download data from the service is in XML
    format.  The package's main function transforms that XML data into a numeric 
    data frame with treasury product items (constant maturity yields for 12 kinds 
    of bills, notes, and bonds) as columns and dates as row names. The function 
    returns a list which includes an item for this data frame as well as query-related
    values for reference and the update date from the service.
	"""
	
	homepage = "https://github.com/mrbcuda/ustyc"
	cran = "ustyc" 

	version("1.0.0", md5="97669c1329913f92ed818a976696377b")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
