# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsprep(RPackage):
	"""Package for Summarizing, Filtering, Imputing, and Normalizing Metabolomics Data

	Package performs summarization of replicates, filtering by frequency, several different options for imputing missing data, and a variety of options for transforming, batch correcting, and normalizing data.
	"""
	
	homepage = "https://github.com/KechrisLab/MSPrep"
	bioc = "MSPrep"

	version("1.18.0", commit="556b08ab0844d8240f7eb03d00aba3fa1c0ee7d7")
	version("1.12.0", commit="511dcda3ad4399e69a9c3d46a50e9749f320e6b2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-pcamethods@1.24:", type=("build", "run"))
	depends_on("r-crmn", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
