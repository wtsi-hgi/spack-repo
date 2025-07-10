# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumantranscriptomecompendium(RPackage):
	"""Tools to work with a Compendium of 181000 human transcriptome sequencing studies

	Provide tools for working with a compendium of human transcriptome sequences (originally htxcomp).
	"""
	
	bioc = "HumanTranscriptomeCompendium" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HumanTranscriptomeCompendium_1.17.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HumanTranscriptomeCompendium/HumanTranscriptomeCompendium_1.17.0.tar.gz"]

	version("1.17.0", sha256="5ba92aca4d359d78bd5252836a979503080e45163549d0abee23c409c1ef7404")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ssrch", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
