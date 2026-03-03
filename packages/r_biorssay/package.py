# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiorssay(RPackage):
	"""Analyze Bioassays and Probit Graphs

	A robust framework for analyzing mortality data from bioassays for one or several strains/lines/populations.
	"""
	
	homepage = "https://milesilab.github.io/BioRssay/"
	cran = "BioRssay" 

	version("1.1.0", md5="9bfd433487fa6df37fb4c0c698ef83f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
