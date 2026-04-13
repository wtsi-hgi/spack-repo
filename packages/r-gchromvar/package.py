# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGchromvar(RPackage):
	"""Compute Cell-Type Specific Enrichments with High Resolution.

	R package for computing cell-type specific GWAS enrichments from
	finemapping and quantitative epigenomic data."""

	homepage = "https://github.com/caleblareau/gchromVAR"
	git = "https://github.com/caleblareau/gchromVAR.git"

	version("20200115", commit="e4f33cad4115160ee4bdf16fd625c2fcd0bf3910")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-chromvar", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
