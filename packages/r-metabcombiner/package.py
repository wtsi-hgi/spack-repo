# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabcombiner(RPackage):
	"""Method for Combining LC-MS Metabolomics Feature Measurements

	This package aligns LC-HRMS metabolomics datasets acquired from biologically similar specimens analyzed under similar, but not necessarily identical, conditions. Peak-picked and simply aligned metabolomics feature tables (consisting of m/z, rt, and per-sample abundance measurements, plus optional identifiers & adduct annotations) are accepted as input. The package outputs a combined table of feature pair alignments, organized into groups of similar m/z, and ranked by a similarity score. Input tables are assumed to be acquired using similar (but not necessarily identical) analytical methods.
	"""
	
	bioc = "metabCombiner" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metabCombiner_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metabCombiner/metabCombiner_1.12.0.tar.gz"]

	version("1.12.0", sha256="b8493d5575c05813090b06029e9b675506fba311d0484f896f5d00709dfa31c6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
