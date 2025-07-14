# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtreemix(RPackage):
	"""Rtreemix: Mutagenetic trees mixture models.

	Rtreemix is a package that offers an environment for estimating the mutagenetic trees mixture models from cross-sectional data and using them for various predictions. It includes functions for fitting the trees mixture models, likelihood computations, model comparisons, waiting time estimations, stability analysis, etc.
	"""
	
	bioc = "Rtreemix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rtreemix_1.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rtreemix/Rtreemix_1.64.0.tar.gz"]

	version("1.70.0", tag="RELEASE_3_21")
	version("1.64.0", sha256="e57f94f6a2327d4579a5adc9937806c7fac244773d84ed3a7f4490aae25aca5d")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
