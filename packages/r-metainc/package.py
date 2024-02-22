# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetainc(RPackage):
	"""Assessment of Inconsistency in Meta-Analysis using Decision
Thresholds

	Assessment of inconsistency in meta-analysis by calculating the Decision Inconsistency index (DI) and the Across-Studies Inconsistency (ASI) index. These indices quantify inconsistency taking into account outcome-level decision thresholds.
	"""
	
	cran = "metainc" 

	version("0.2-0", md5="77f931a9e6ec36867827e95a5283b9e7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-meta@7.0.0:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-confintr", type=("build", "run"))
