# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrackviewer(RPackage):
	"""A R/Bioconductor package with web interface for drawing elegant interactive tracks or lollipop plot to facilitate integrated analysis of multi-omics data

	Visualize mapped reads along with annotation as track layers for NGS dataset such as ChIP-seq, RNA-seq, miRNA-seq, DNA-seq, SNPs and methylation data.
	"""
	
	bioc = "trackViewer"

	version("1.44.0", commit="df30c4bbab113a785acf6119339bf0ad5a5b4ab7")
	version("1.38.2", commit="9e62dddda6311011bd3cd72c2cc37c5ad9b48cc9")
	version("1.38.1", md5="c0004e0bdb49b5d051e486f73a79a245")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-grimport", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-strawr", type=("build", "run"))
