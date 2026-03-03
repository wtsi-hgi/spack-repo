# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRflptools(RPackage):
	"""Tools to Analyse RFLP Data

	Provides functions to analyse DNA fragment samples (i.e. derived from RFLP-analysis) and standalone BLAST report files (i.e. DNA sequence analysis).
	"""
	
	cran = "RFLPtools" 

	version("2.0", md5="7f2f5d8432808f76bca1353ff1b0324d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
