# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhsage(RPackage):
	"""Reproductive Age Female Data of Various Demographic Health
Surveys

	We provide 70 data sets of females of reproductive age from 19 Asian countries, ranging in age from 15 to 49. The data sets are extracted from demographic and health surveys that were conducted over an extended period of time. Moreover, the functions also provide Whipple’s index as well as age reporting quality such as very rough, rough, approximate, accurate, and highly accurate.
	"""
	
	cran = "dhsage" 

	version("0.1.0", md5="011fcfb232ac34d06c2defd264d0cc75")

	depends_on("r@4:", type=("build", "run"))
