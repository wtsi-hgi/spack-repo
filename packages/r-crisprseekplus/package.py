# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprseekplus(RPackage):
	"""crisprseekplus

	Bioinformatics platform containing interface to work with offTargetAnalysis and compare2Sequences in the CRISPRseek package, and GUIDEseqAnalysis.
	"""
	
	homepage = "https://github.com/UMMS-Biocore/crisprseekplus"
	bioc = "crisprseekplus" 

	version("1.28.0", commit="8338d72d8b6a58c6a9dcceec3fdf3888de66e59e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-crisprseek", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-guideseq", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
