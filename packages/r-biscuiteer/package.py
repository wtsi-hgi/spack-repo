# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiscuiteer(RPackage):
	"""Convenience Functions for Biscuit

	A test harness for bsseq loading of Biscuit output, summarization of WGBS data over defined regions and in mappable samples, with or without imputation, dropping of mostly-NA rows, age estimates, etc.
	"""
	
	homepage = "https://github.com/trichelab/biscuiteer"
	bioc = "biscuiteer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biscuiteer_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biscuiteer/biscuiteer_1.16.0.tar.gz"]

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="f177fd484cee8ed17889d637759e343626e1cb41b8f3bd98f9f4168949b820e1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biscuiteerdata", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-qualv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-mus-musculus", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))
	depends_on("r-dmrseq", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
