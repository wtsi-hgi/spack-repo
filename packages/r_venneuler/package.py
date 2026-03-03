# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVenneuler(RPackage):
	"""Venn and Euler Diagrams

	Calculates and displays Venn and Euler Diagrams.
	"""
	
	homepage = "https://www.rforge.net/venneuler/"
	cran = "venneuler" 

	version("1.1-4", md5="2439fa70ea80629fee02e756c9ab52c3")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))
