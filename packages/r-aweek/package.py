# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAweek(RPackage):
	"""Convert Dates to Arbitrary Week Definitions

	Which day a week starts depends heavily on the either the local or
  professional context. This package is designed to be a lightweight solution
  to easily switching between week-based date definitions. 
	"""
	
	homepage = "https://www.repidemicsconsortium.org/aweek/"
	cran = "aweek" 

	version("1.0.3", md5="a78145b85e07069a6d9e8cd33d575499")

	depends_on("r@3:", type=("build", "run"))
