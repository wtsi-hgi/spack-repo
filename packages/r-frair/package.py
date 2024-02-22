# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrair(RPackage):
	"""Tools for Functional Response Analysis

	Tools to support sensible statistics for functional response analysis.
	"""
	
	homepage = "https://github.com/dpritchard/frair"
	cran = "frair" 

	version("0.5.100", md5="ae8fbe794cf0f8067ffdc503bbf27fca")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-lamw@1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
