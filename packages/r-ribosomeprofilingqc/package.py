# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibosomeprofilingqc(RPackage):
	"""Ribosome Profiling Quality Control

	Ribo-Seq (also named ribosome profiling or footprinting) measures translatome (unlike RNA-Seq, which sequences the transcriptome) by direct quantification of the ribosome-protected fragments (RPFs). This package provides the tools for quality assessment of ribosome profiling. In addition, it can preprocess Ribo-Seq data for subsequent differential analysis.
	"""
	
	bioc = "ribosomeProfilingQC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ribosomeProfilingQC_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ribosomeProfilingQC/ribosomeProfilingQC_1.14.1.tar.gz"]

	version("1.14.1", md5="0e8192f66f9ba7110763755200edee3a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-edaseq", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-ruvseq", type=("build", "run"))
	depends_on("r-rsubread", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
