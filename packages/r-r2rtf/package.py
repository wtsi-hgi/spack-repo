# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2rtf(RPackage):
	"""Easily Create Production-Ready Rich Text Format (RTF) Table and
Figure

	Create production-ready Rich Text Format (RTF) table and figure
    with flexible format.
	"""
	
	homepage = "https://merck.github.io/r2rtf/"
	cran = "r2rtf" 

	version("1.1.1", md5="9d62b3fb3e13298f3f7762d11f848f57")

	depends_on("r@3.5:", type=("build", "run"))
