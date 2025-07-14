# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsealm(RPackage):
	"""Linear Model Toolset for Gene Set Enrichment Analysis

	Models and methods for fitting linear models to gene expression data, together with tools for computing and using various regression diagnostics.
	"""
	
	bioc = "GSEAlm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSEAlm_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSEAlm/GSEAlm_1.62.0.tar.gz"]

    version("1.68.0", tag="RELEASE_3_21")
	version("1.62.0", sha256="08e34285f60eb07ceda3ce3e78a9f7be1afce4716f12d73efe168b7e5e91aa46")

	depends_on("r-biobase", type=("build", "run"))
