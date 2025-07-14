# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcnv(RPackage):
	"""Integrated Copy Number Variation detection

	Integrative copy number variation (CNV) detection from multiple platform and experimental design.
	"""
	
	bioc = "iCNV" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iCNV_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iCNV/iCNV_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="098e5db84bc200cd6518f02f7bdd7521a6d8fad8fe58c9f7130f730f6cbda085")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-codex", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
