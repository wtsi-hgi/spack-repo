# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtar(RPackage):
	"""Multi-Trait Analysis of Rare-Variant Association Study

	Perform multi-trait rare-variant association tests using the summary statistics and adjust for possible sample overlap. Package is based on "Multi-Trait Analysis of Rare-Variant Association Summary Statistics using MTAR" by Luo, L., Shen, J., Zhang, H., Chhibber, A. Mehrotra, D.V., Tang, Z., 2019 (submitted).
	"""
	
	cran = "MTAR" 

	version("0.1.1", md5="0604736b980d3de248c881b09e173c9d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-compquadform@1.4.3:", type=("build", "run"))
	depends_on("r-mass@7.3.51.4:", type=("build", "run"))
	depends_on("r-matrix@1.2.2:", type=("build", "run"))
