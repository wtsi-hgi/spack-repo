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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GeuvadisTranscriptExpr_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GeuvadisTranscriptExpr/GeuvadisTranscriptExpr_1.30.0.tar.gz"]

	version("1.30.0", md5="806de22bef0659a3b6f9db122d87a1d6")

	depends_on("r@3.5:", type=("build", "run"))

