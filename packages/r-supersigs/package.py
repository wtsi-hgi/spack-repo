# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupersigs(RPackage):
	"""Supervised mutational signatures

	Generate SuperSigs (supervised mutational signatures) from single nucleotide variants in the cancer genome. Functions included in the package allow the user to learn supervised mutational signatures from their data and apply them to new data. The methodology is based on the one described in Afsari (2021, ELife).
	"""
	
	homepage = "https://tomasettilab.github.io/supersigs/"
	bioc = "supersigs" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/supersigs_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/supersigs/supersigs_1.10.0.tar.gz"]

	version("1.10.0", md5="35df3e9fd0272854b23baf15d93d300f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
