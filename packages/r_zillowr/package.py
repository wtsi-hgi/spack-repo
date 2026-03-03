# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZillowr(RPackage):
	"""R Interface to Zillow Real Estate and Mortgage Data API

	Zillow, an online real estate company, provides real estate
    and mortgage data for the United States through a REST API. The
    ZillowR package provides an R function for each API service, making it
    easy to make API calls and process the response into convenient,
    R-friendly data structures.  See
    <https://www.zillow.com/howto/api/APIOverview.htm> for the Zillow API
    Documentation. NOTE: Zillow deprecated their API on 2021-09-30, and
    this package is now deprecated as a result.
	"""
	
	homepage = "https://fascinatingfingers.gitlab.io/zillowr"
	cran = "ZillowR" 

	version("1.0.0", md5="cbf5bd26b701767e3f1a1e75380dd080")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
