# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipanalyser(RPackage):
	"""ChIPanalyser: Predicting Transcription Factor Binding Sites

	ChIPanalyser is a package to predict and understand TF binding by utilizing a statistical thermodynamic model. The model incorporates 4 main factors thought to drive TF binding: Chromatin State, Binding energy, Number of bound molecules and a scaling factor modulating TF binding affinity. Taken together, ChIPanalyser produces ChIP-like profiles that closely mimic the patterns seens in real ChIP-seq data.
	"""
	
	bioc = "ChIPanalyser" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ChIPanalyser_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ChIPanalyser/ChIPanalyser_1.24.0.tar.gz"]

	version("1.24.0", sha256="1b11a1a7aef3df7693f4a00d44995e08fed16987d581301392d9df50985b56c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
