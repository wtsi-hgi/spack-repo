# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToordinal(RPackage):
	"""Cardinal to Ordinal Number & Date Conversion

	Language specific cardinal to ordinal number conversion.
	"""
	
	homepage = "https://centerforassessment.github.io/toOrdinal/"
	cran = "toOrdinal" 

	version("1.3-0.0", md5="ab70f953cfe6ce1082edbe2906d74254")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
