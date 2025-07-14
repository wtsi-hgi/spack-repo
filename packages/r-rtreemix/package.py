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

	version("1.70.0", commit="c68fcf9893ac4772580cd41692d7a93579a5debe")
	version("1.64.0", commit="57e80b142324d4403959b00c0e3afae99f3dee85")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
