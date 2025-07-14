# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellscore(RPackage):
	"""Tool for Evaluation of Cell Identity from Transcription Profiles

	The CellScore package contains functions to evaluate the cell identity of a test sample, given a cell transition defined with a starting (donor) cell type and a desired target cell type. The evaluation is based upon a scoring system, which uses a set of standard samples of known cell types, as the reference set. The functions have been carried out on a large set of microarray data from one platform (Affymetrix Human Genome U133 Plus 2.0). In principle, the method could be applied to any expression dataset, provided that there are a sufficient number of standard samples and that the data are normalized.
	"""
	
	bioc = "CellScore"

	version("1.28.0", commit="9ca9b34ba16638b20b53f294cece83b92b06353f")
	version("1.22.0", commit="41884526e0daf8f46aac006de75bde2c86e986ab")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase@2.39.1:", type=("build", "run"))
	depends_on("r-gplots@3.0.1:", type=("build", "run"))
	depends_on("r-lsa@0.73.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-squash@1.0.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
