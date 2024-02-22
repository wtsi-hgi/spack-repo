# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScploidy(RPackage):
	"""Infer Ploidy of Single Cells

	Compute ploidy of single cells (or nuclei)
    based on single-cell (or single-nucleus)
    ATAC-seq (Assay for Transposase-Accessible Chromatin using sequencing)
    data <https://github.com/fumi-github/scPloidy>.
	"""
	
	cran = "scPloidy" 

	version("0.3.0", md5="78259846ab0f9bbf514c423b15ec5e2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
