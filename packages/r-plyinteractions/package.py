# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlyinteractions(RPackage):
	"""Extending tidy verbs to genomic interactions

	Operate on `GInteractions` objects as tabular data using `dplyr`-like verbs. The functions and methods in `plyinteractions` provide a grammatical approach to manipulate `GInteractions`, to facilitate their integration in genomic analysis workflows.
	"""
	
	homepage = "https://github.com/js2264/plyinteractions"
	bioc = "plyinteractions"

	version("1.6.0", commit="430eacd68cf77c5c9ce8f206f14b90854ea56d4a")
	version("1.0.0", commit="ee766a19912132c8fdb9a52c248e88d2bf0c84e9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
