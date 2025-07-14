# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventpointer(RPackage):
	"""An effective identification of alternative splicing events using junction arrays and RNA-Seq data

	EventPointer is an R package to identify alternative splicing events that involve either simple (case-control experiment) or complex experimental designs such as time course experiments and studies including paired-samples. The algorithm can be used to analyze data from either junction arrays (Affymetrix Arrays) or sequencing data (RNA-Seq). The software returns a data.frame with the detected alternative splicing events: gene name, type of event (cassette, alternative 3',...,etc), genomic position, statistical significance and increment of the percent spliced in (Delta PSI) for all the events. The algorithm can generate a series of files to visualize the detected alternative splicing events in IGV. This eases the interpretation of results and the design of primers for standard PCR validation.
	"""
	
	bioc = "EventPointer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EventPointer_3.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EventPointer/EventPointer_3.10.0.tar.gz"]

	version("3.16.0", tag="RELEASE_3_21")
	version("3.10.0", sha256="e49e6dc9ae689350b776fc122a90700bd4531b659c3d7d3d1cc36b4ad76a6297")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sgseq", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-affxparser", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-poibin", type=("build", "run"))
	depends_on("r-speedglm", type=("build", "run"))
	depends_on("r-tximport", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
