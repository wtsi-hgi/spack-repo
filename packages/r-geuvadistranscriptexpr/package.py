# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeuvadistranscriptexpr(RPackage):
	"""Data package with transcript expression and bi-allelic genotypes from the GEUVADIS project

	Provides transcript expression and bi-allelic genotypes corresponding to the chromosome 19 for CEU individuals from the GEUVADIS project, Lappalainen et al.
	"""
	
	bioc = "GeuvadisTranscriptExpr"

	version("1.36.0", commit="2a8d54db95ccba52cedfde231cd2c1d101c1e086")
	version("1.30.0", commit="de40a69a39f1dd79966db93112ba879f6b29b2ea")

	depends_on("r@3.5:", type=("build", "run"))

