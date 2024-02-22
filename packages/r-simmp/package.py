# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmp(RPackage):
	"""Simulate Somatic Mutations in Cancer Genomes from Mutational
Processes

	Simulates somatic single base substitutions carried in cancer genomes. By only providing a human reference genome, substitutions that result from mutational processes operative in every cancer genome can be generated.
	"""
	
	cran = "simMP" 

	version("0.17.3", md5="b56e2056fb586989fe7e1f264a91cf3f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
