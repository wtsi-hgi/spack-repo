# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndia(RPackage):
	"""Influence Diagnostics in Statistical Models

	Set of routines for influence diagnostics by using case-deletion in ordinary least 
    squares, ridge estimation [Walker and Birch (1988). <doi:10.1080/00401706.1988.10488370>] and 
    least absolute deviations (LAD) regression [Sun and Wei (2004). <doi:10.1016/j.spl.2003.08.018>].
	"""
	
	cran = "india" 

	version("0.1", md5="c90ed8cd69f72ea19ddbadd7d7359646")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastmatrix", type=("build", "run"))
	depends_on("r-l1pack", type=("build", "run"))
