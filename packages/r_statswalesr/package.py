# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatswalesr(RPackage):
	"""Easily Extract Data from 'StatsWales'

	Download data from 'StatsWales' into R. Removes the need for the user to
    write their own loops when parsing data from the 'StatsWales' API. Provides functions
    for datasets (<http://open.statswales.gov.wales/en-gb/dataset>) and metadata
    (<http://open.statswales.gov.wales/en-gb/discover/metadata>) endpoints. 
	"""
	
	cran = "statswalesr" 

	version("0.2.0", md5="ef402e1e252c5a28d994767bfb701a54")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
