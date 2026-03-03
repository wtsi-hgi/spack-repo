# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafetydata(RPackage):
	"""Clinical Trial Data

	Example clinical trial data sets formatted for easy use in R.
	"""
	
	cran = "safetyData" 

	version("1.0.0", md5="d8fd9c263e75b935083996a1dcf8409e")

	depends_on("r@3:", type=("build", "run"))
