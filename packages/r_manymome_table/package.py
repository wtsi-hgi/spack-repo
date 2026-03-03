# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManymomeTable(RPackage):
	"""Publication-Ready Tables for 'manymome' Results

	Converts results from the 'manymome' package,
  presented in Cheung and Cheung (2023)
  <doi:10.3758/s13428-023-02224-z>, to publication-ready
  tables.
	"""
	
	homepage = "https://sfcheung.github.io/manymome.table/"
	cran = "manymome.table" 

	version("0.3.0", md5="46b43e212b760608f10d91edc97f546d")
	version("0.2.0", md5="3ed782547b6d472e0b11199adb73db73")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-manymome", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
