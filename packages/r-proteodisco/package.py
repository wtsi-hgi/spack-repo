# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteodisco(RPackage):
	"""Generation of customized protein variant databases from genomic variants, splice-junctions and manual sequences

	ProteoDisco is an R package to facilitate proteogenomics studies. It houses functions to create customized (variant) protein databases based on user-submitted genomic variants, splice-junctions, fusion genes and manual transcript sequences. The flexible workflow can be adopted to suit a myriad of research and experimental settings.
	"""
	
	homepage = "https://github.com/ErasmusMC-CCBC/ProteoDisco"
	bioc = "ProteoDisco"

	version("1.14.0", commit="b2805908a85cfde8491d59e193bc1672679d44be")
	version("1.8.0", commit="678154ab1e7e9865ebc965f9f222a00bff8ce8a2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocgenerics@0.38:", type=("build", "run"))
	depends_on("r-biocparallel@1.26:", type=("build", "run"))
	depends_on("r-biostrings@2.60.1:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-cleaver@1.30:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.28:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.44:", type=("build", "run"))
	depends_on("r-genomicranges@1.44:", type=("build", "run"))
	depends_on("r-iranges@2.26:", type=("build", "run"))
	depends_on("r-parallellogger@2.0.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-s4vectors@0.30:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-variantannotation@1.36:", type=("build", "run"))
	depends_on("r-xvector@0.32:", type=("build", "run"))
