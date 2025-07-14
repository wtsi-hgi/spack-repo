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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CellScore_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CellScore/CellScore_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="500fca2a0296c684f92bb1f5eededade31bcee140a6e9a28df7687b31f00506a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase@2.39.1:", type=("build", "run"))
	depends_on("r-gplots@3.0.1:", type=("build", "run"))
	depends_on("r-lsa@0.73.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-squash@1.0.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
