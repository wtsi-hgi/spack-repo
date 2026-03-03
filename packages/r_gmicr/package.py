# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmicr(RPackage):
	"""Combines WGCNA and xCell readouts with bayesian network learrning to generate a Gene-Module Immune-Cell network (GMIC)

	This package uses bayesian network learning to detect relationships between Gene Modules detected by WGCNA and immune cell signatures defined by xCell. It is a hypothesis generating tool.
	"""
	
	bioc = "GmicR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GmicR_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GmicR/GmicR_1.16.0.tar.gz"]

	version("1.16.0", md5="13466f8e105c84116d73b39d38eed3cd")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-grain", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
