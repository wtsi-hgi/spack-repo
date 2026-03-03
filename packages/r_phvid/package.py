# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhvid(RPackage):
	"""PharmacoVigilance Signal Detection

	A collection of several pharmacovigilance signal detection methods extended to the multiple comparison setting.
	"""
	
	cran = "PhViD" 

	version("1.0.8", md5="ed061a264892e9a4444d7912cdce61cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lbe", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("tcl", type=("build", "link", "run"))
	depends_on("tk", type=("build", "link", "run"))
	depends_on("tktable", type=("build", "link", "run"))
