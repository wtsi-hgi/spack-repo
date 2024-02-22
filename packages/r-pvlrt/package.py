# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvlrt(RPackage):
	"""Likelihood Ratio Test-Based Approaches to Pharmacovigilance

	A suite of likelihood ratio test based methods to use in pharmacovigilance. Contains various testing and post-processing functions.
	"""
	
	cran = "pvLRT" 

	version("0.5.1", md5="042de64d5425490a9c8b0a22dbdabf0f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
