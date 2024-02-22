# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopgenr(RPackage):
	"""Accompaniment to Population Genetics with R: An Introduction for
Life Scientists

	Provides several data sets and functions to accompany the book "Population Genetics with R: An Introduction for Life Scientists" (2021, ISBN:9780198829546).
	"""
	
	homepage = "https://global.oup.com/academic/product/population-genetics-with-r-9780198829546?cc=gb&lang=en#"
	cran = "popgenr" 

	version("0.2", md5="e044f4f4edec9deeeda6e2ec1bf9c2c4")

	depends_on("r@3.5:", type=("build", "run"))
