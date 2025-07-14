# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiky(RPackage):
	"""Spike-in calibration for cell-free MeDIP

	spiky implements methods and model generation for cfMeDIP (cell-free methylated DNA immunoprecipitation) with spike-in controls. CfMeDIP is an enrichment protocol which avoids destructive conversion of scarce template, making it ideal as a "liquid biopsy," but creating certain challenges in comparing results across specimens, subjects, and experiments. The use of synthetic spike-in standard oligos allows diagnostics performed with cfMeDIP to quantitatively compare samples across subjects, experiments, and time points in both relative and absolute terms.
	"""
	
	homepage = "https://github.com/trichelab/spiky"
	bioc = "spiky"

	version("1.14.0", commit="cdb4edc410af3b98c5853e7bf0e1a2098bc4c201")
	version("1.8.0", commit="9732d5212371d7230c318ff334aeade21bb003fc")

	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bamlss", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-blandaltmanleh", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
