# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrgenomics(RPackage):
	"""Tools for the Efficient Analysis of High-Resolution Genomics Data

	This package provides useful and efficient utilites for the analysis of high-resolution genomic data using standard Bioconductor methods and classes. BRGenomics is feature-rich and simplifies a number of post-alignment processing steps and data handling. Emphasis is on efficient analysis of multiple datasets, with support for normalization and blacklisting. Included are functions for: spike-in normalizing data; generating basepair-resolution readcounts and coverage data (e.g. for heatmaps); importing and processing bam files (e.g. for conversion to bigWig files); generating metaplots/metaprofiles (bootstrapped mean profiles) with confidence intervals; conveniently calling DESeq2 without using sample-blind estimates of genewise dispersion; among other features.
	"""
	
	homepage = "https://mdeber.github.io"
	bioc = "BRGenomics"

	version("1.14.1", commit="bbd90bff44fbb6173a8761f568ae143523cae252")
	version("1.13.0", md5="33a9bc55e58468faa4cc337617be743a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
