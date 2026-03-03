# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbursts(RPackage):
	"""Single Channel Bursts Analysis

	Provides tools to import and export from several existing pieces of ion-channel analysis software such as 'TAC', 'QUB', 'SCAN', and 'Clampfit', implements procedures such as dwell-time correction and defining bursts with a critical time, and provides tools for analysis of bursts, such as tools for sorting and plotting.
	"""
	
	cran = "scbursts" 

	version("1.6", md5="7c87de5b545521c3b508a7bf5d8d840a")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
