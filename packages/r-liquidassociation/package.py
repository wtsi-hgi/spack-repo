# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiquidassociation(RPackage):
	"""LiquidAssociation

	The package contains functions for calculate direct and model-based estimators for liquid association. It also provides functions for testing the existence of liquid association given a gene triplet data.
	"""
	
	bioc = "LiquidAssociation" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LiquidAssociation_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LiquidAssociation/LiquidAssociation_1.56.0.tar.gz"]

	version("1.56.0", sha256="eb8f1f63a53bcfb14143f6c0760304eadf6ec249ae4914a2fc9c14ce04056202")

	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-yeastcc", type=("build", "run"))
	depends_on("r-org-sc-sgd-db", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
