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

	version("1.42.0", commit="94a447228201f49169269b2e821eb24efe5b6372")
	version("1.36.0", commit="6cc82626ad034471d2bf22dabf96bd96ebd70b59")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
