# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdm(RPackage):
	"""Generalized Dissimilarity Modeling

	A toolkit with functions to fit, plot, summarize, and apply Generalized Dissimilarity Models. Mokany K, Ware C, Woolley SNC, Ferrier S, Fitzpatrick MC (2022) <doi:10.1111/geb.13459> Ferrier S, Manion G, Elith J, Richardson K (2007) <doi:10.1111/j.1472-4642.2007.00341.x>.
	"""
	
	homepage = "https://mfitzpatrick.al.umces.edu/gdm/"
	cran = "gdm" 

	version("1.5.0-9.1", md5="49d50be56c6bf4053d2da564249aeb6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
