# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytodx(RPackage):
	"""Robust prediction of clinical outcomes using cytometry data without cell gating

	This package provides functions that predict clinical outcomes using single cell data (such as flow cytometry data, RNA single cell sequencing data) without the requirement of cell gating or clustering.
	"""
	
	bioc = "CytoDx" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CytoDx_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CytoDx/CytoDx_1.22.0.tar.gz"]

	version("1.22.0", md5="86d2f225be6ebdaecd3aa4960e443796")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
