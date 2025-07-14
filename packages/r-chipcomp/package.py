# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipcomp(RPackage):
	"""Quantitative comparison of multiple ChIP-seq datasets

	ChIPComp detects differentially bound sharp binding sites across multiple conditions considering matching control.
	"""
	
	bioc = "ChIPComp"

	version("1.38.0", commit="6acca5eabbd23cd283bcbf3b789774ea74d395be")
	version("1.32.0", commit="46346bb6c97bcc175c153bc5862f5ce3ec9595c6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm9", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
