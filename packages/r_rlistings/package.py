# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlistings(RPackage):
	"""Clinical Trial Style Data Readout Listings

	Listings are often part of the submission of clinical trial
    data in regulatory settings.  We provide a framework for the specific
    formatting features often used when displaying large datasets in that
    context.
	"""
	
	homepage = "https://github.com/insightsengineering/rlistings"
	cran = "rlistings" 

	version("0.2.7", md5="b15f85079195f7afbb26ffa6a91c160f")

	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
