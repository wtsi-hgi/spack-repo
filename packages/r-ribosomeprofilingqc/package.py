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

	version("1.20.0", commit="b9c10b1efd3b20cdc8324ad7f231a1e8dccb3b71")
	version("1.14.1", commit="9286a0a8c6edbe8432c15b408057a1d677edefe8")

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
