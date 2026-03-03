# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDanielbiostatistics10th(RPackage):
	"""Functions for Wayne W. Daniel's Biostatistics, Tenth Edition

	Functions to accompany Wayne W. Daniel's Biostatistics: A
        Foundation for Analysis in the Health Sciences, Tenth Edition.
	"""
	
	cran = "DanielBiostatistics10th" 

	version("0.1.10", md5="ba1c4d922395b23f4f266926891a38f6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
