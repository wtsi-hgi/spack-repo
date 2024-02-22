# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsocrata(RPackage):
	"""Download or Upload 'Socrata' Data Sets

	Provides easier interaction with
    'Socrata' open data portals <https://dev.socrata.com>.
    Users can provide a 'Socrata' data set resource URL,
    or a 'Socrata' Open Data API (SODA) web query,
    or a 'Socrata' "human-friendly" URL,
    returns an R data frame. Converts dates to 'POSIX'
    format and manages throttling by 'Socrata'.
    Users can upload data to 'Socrata' portals directly
    from R.
	"""
	
	homepage = "https://github.com/Chicago/RSocrata"
	cran = "RSocrata" 

	version("1.7.15-1", md5="8068d84f0e93597f356ef708bd932bf0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-mime@0.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
