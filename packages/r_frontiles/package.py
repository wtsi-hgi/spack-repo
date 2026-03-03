# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrontiles(RPackage):
	"""Partial Frontier Efficiency Analysis

	It calculates the alpha-quantile proposed by Daouia and Simar (2007) <doi:10.1016/j.jeconom.2006.07.002> and order-m efficiency score in multi-dimension proposed by Daouia and Gijbels (2011) <doi:10.1016/j.jeconom.2010.12.002> and computes several summaries and representation of the associated frontiers in 2d and 3d.
	"""
	
	cran = "frontiles" 

	version("1.3.1", md5="790750bd1e11d6cf065938bf48d96902")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
