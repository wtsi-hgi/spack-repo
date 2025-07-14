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

	version("1.16.0", commit="0d4ba4ae1a79f9c978f8606b7bf290fcfc72b442")
	version("1.10.0", commit="51c1733745a86263128339c2bd923e445e374b0c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
