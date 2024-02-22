# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaparsimony(RPackage):
	"""Searching Parsimony Models with Genetic Algorithms

	Methodology that combines feature selection, model tuning, and parsimonious model selection with Genetic Algorithms (GA) proposed in {Martinez-de-Pison} (2015) <DOI:10.1016/j.asoc.2015.06.012>. To this objective, a novel GA selection procedure is introduced based on separate cost and complexity evaluations.
	"""
	
	homepage = "https://github.com/jpison/GAparsimony"
	cran = "GAparsimony" 

	version("0.9.5", md5="cc65a539e3c52b0eeacbed249dbb1d86")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
