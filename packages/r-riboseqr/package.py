# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiboseqr(RPackage):
	"""Analysis of sequencing data from ribosome profiling experiments

	Plotting functions, frameshift detection and parsing of sequencing data from ribosome profiling experiments.
	"""
	
	bioc = "riboSeqR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/riboSeqR_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/riboSeqR/riboSeqR_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="1077844904ab167bd0f57ff5c77fc8439c90749ef9d69a94bc111c76c75d2fb2")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
