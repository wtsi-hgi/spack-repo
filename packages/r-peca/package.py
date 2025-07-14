# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeca(RPackage):
	"""Probe-level Expression Change Averaging

	Calculates Probe-level Expression Change Averages (PECA) to identify differential expression in Affymetrix gene expression microarray studies or in proteomic studies using peptide-level mesurements respectively.
	"""
	
	bioc = "PECA"

	version("1.44.0", commit="c9dfef7bf0f6a12b5dc66e06bc7b3b583c6ed631")
	version("1.38.0", commit="5fa3be42309b1f05f8972cee88124e6f73edfd2c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rots", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-aroma-affymetrix", type=("build", "run"))
	depends_on("r-aroma-core", type=("build", "run"))
