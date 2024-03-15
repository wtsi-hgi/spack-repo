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

	version("1.36.0", md5="eb9c84e564128ad11960fac5955c4d2f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
