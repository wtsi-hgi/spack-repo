# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtrace(RPackage):
	"""Trace and Highlight Groups of Data Points

	Provides 'ggplot2' geoms that allow groups of data points to be
    outlined or highlighted for emphasis. This is particularly useful when
    working with dense datasets that are prone to overplotting.
	"""
	
	homepage = "https://github.com/rnabioco/ggtrace"
	cran = "ggtrace" 

	version("0.2.0", md5="42827b97292c0f2235b270c7032f2ec8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
