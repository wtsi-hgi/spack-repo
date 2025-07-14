# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMslp(RPackage):
	"""Predict synthetic lethal partners of tumour mutations

	An integrated pipeline to predict the potential synthetic lethality partners (SLPs) of tumour mutations, based on gene expression, mutation profiling and cell line genetic screens data. It has builtd-in support for data from cBioPortal. The primary SLPs correlating with muations in WT and compensating for the loss of function of mutations are predicted by random forest based methods (GENIE3) and Rank Products, respectively. Genetic screens are employed to identfy consensus SLPs leads to reduced cell viability when perturbed.
	"""
	
	bioc = "mslp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mslp_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mslp/mslp_1.4.0.tar.gz"]

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="d3647c9e496698ca1f287e9d24d112c833622bc40dca683bb997af3d43768ac4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rankprod", type=("build", "run"))
