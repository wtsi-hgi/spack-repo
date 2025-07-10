# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCagefightr(RPackage):
	"""Analysis of Cap Analysis of Gene Expression (CAGE) data using Bioconductor

	CAGE is a widely used high throughput assay for measuring transcription start site (TSS) activity. CAGEfightR is an R/Bioconductor package for performing a wide range of common data analysis tasks for CAGE and 5'-end data in general. Core functionality includes: import of CAGE TSSs (CTSSs), tag (or unidirectional) clustering for TSS identification, bidirectional clustering for enhancer identification, annotation with transcript and gene models, correlation of TSS and enhancer expression, calculation of TSS shapes, quantification of CAGE expression as expression matrices and genome brower visualization.
	"""
	
	homepage = "https://github.com/MalteThodberg/CAGEfightR"
	bioc = "CAGEfightR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CAGEfightR_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CAGEfightR/CAGEfightR_1.22.0.tar.gz"]

	version("1.22.0", sha256="80fd09e31d654bac277962dfee644c4b09ef3a0148c14b8ee51147f2f4cf7d41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges@1.30.1:", type=("build", "run"))
	depends_on("r-rtracklayer@1.38.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.8.1:", type=("build", "run"))
	depends_on("r-pryr@0.1.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.12:", type=("build", "run"))
	depends_on("r-biocgenerics@0.24:", type=("build", "run"))
	depends_on("r-s4vectors@0.16:", type=("build", "run"))
	depends_on("r-iranges@2.12:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.14:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.29.11:", type=("build", "run"))
	depends_on("r-genomicalignments@1.22.1:", type=("build", "run"))
	depends_on("r-biocparallel@1.12:", type=("build", "run"))
	depends_on("r-genomicfiles@1.14:", type=("build", "run"))
	depends_on("r-gviz@1.22.2:", type=("build", "run"))
	depends_on("r-interactionset@1.9.4:", type=("build", "run"))
	depends_on("r-genomicinteractions@1.15.1:", type=("build", "run"))
