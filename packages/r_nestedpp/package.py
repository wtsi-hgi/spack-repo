# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestedpp(RPackage):
	"""Performance Profiles and Nested Performance Profiles

	Library to plot performance profiles (Dolan and More (2002) <doi:10.1007/s101070100263>) and nested performance profiles (Hekmati and Mirhajianmoghadam (2019) <doi:10.19139/soic-2310-5070-679>) for a given data frame.
	"""
	
	cran = "nestedpp" 

	version("0.2.0", md5="7b0c2fc2535b165f2c1f58e641b236f9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
