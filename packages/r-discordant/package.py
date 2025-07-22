# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscordant(RPackage):
	"""The Discordant Method: A Novel Approach for Differential Correlation

	Discordant is an R package that identifies pairs of features that correlate differently between phenotypic groups, with application to -omics data sets. Discordant uses a mixture model that “bins” molecular feature pairs based on their type of coexpression or coabbundance. Algorithm is explained further in "Differential Correlation for Sequencing Data"" (Siska et al. 2016).
	"""
	
	homepage = "https://github.com/siskac/discordant"
	bioc = "discordant" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/discordant_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/discordant/discordant_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="32c0b5f7d6eafa8de9dabd1dcb64aaa166dd81f1e0a360e6d7acba94889d0a12")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biwt", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
