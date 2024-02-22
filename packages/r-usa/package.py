# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsa(RPackage):
	"""Updated US State Facts and Figures

	Updated versions of the 1970's "US State Facts and
    Figures" objects from the 'datasets' package included with R. The new
    data is compiled from a number of sources, primarily from United
    States Census Bureau or the relevant federal agency.
	"""
	
	homepage = "https://kiernann.com/usa"
	cran = "usa" 

	version("0.1.0", md5="90853d9cacb5938d1b0729159e11c1a5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
