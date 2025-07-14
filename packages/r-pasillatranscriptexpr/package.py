# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasillatranscriptexpr(RPackage):
	"""Data package with transcript expression obtained with kallisto from pasilla knock-down RNA-Seq data from Brooks et al.

	Provides kallisto workflow and transcript expression of RNA-Seq data from Brooks et al.
	"""
	
	bioc = "PasillaTranscriptExpr" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PasillaTranscriptExpr_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PasillaTranscriptExpr/PasillaTranscriptExpr_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="598f8067bc2d258617b55a7ed35c26f68d7a99e3cdcdedc635eced86af17889c")

	depends_on("r@3.3:", type=("build", "run"))

