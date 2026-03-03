# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimms(RPackage):
	"""Subnetwork Integration for Multi-Modal Signatures

	Algorithms to create prognostic biomarkers using biological genesets or networks.
	"""
	
	cran = "SIMMS" 

	version("1.3.2", md5="5b359234332434ef4d55e663e46015ec")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-survival@2.36.2:", type=("build", "run"))
	depends_on("r-mass@7.3.12:", type=("build", "run"))
	depends_on("r-glmnet@1.9.8:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-randomforestsrc@2.9.1:", type=("build", "run"))
