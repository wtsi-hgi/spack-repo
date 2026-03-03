# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsdata(RPackage):
	"""Data on the States and Counties of the United States

	Demographic data on the United States at the county and state levels spanning multiple years.
	"""
	
	homepage = "https://github.com/OpenIntroStat/usdata"
	cran = "usdata" 

	version("0.2.0", md5="2b7a65dcf82fc3aa461b560c2291b0e5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
