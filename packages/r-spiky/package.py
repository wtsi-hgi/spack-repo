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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spiky_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spiky/spiky_1.8.0.tar.gz"]

	version("1.8.0", sha256="438d278282b002765c79ab10b470ef08c96c5efcff11e96496eb754410a1cc87")

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
