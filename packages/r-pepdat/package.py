# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepdat(RPackage):
	"""Peptide microarray data package

	Provides sample files and data for the vignettes of pepStat and Pviz as well as peptide collections for HIV and SIV.
	"""
	
	bioc = "pepDat"

	version("1.28.0", commit="4c98752151c7e8b5f77fa8ad66c6bc16562710ea")
	version("1.22.0", commit="c230a94b649a0fce679e1d015f435c52e3bbdada")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

