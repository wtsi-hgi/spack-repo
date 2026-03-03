# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatingscalereduction(RPackage):
	"""Rating Scale Reduction Procedure

	Describes a new procedure of reducing items in a rating scale called Rating Scale Reduction (RSR). The new stop criterion in RSR procedure is added (stop global max). The function order is replaced by sort.list.
	"""
	
	cran = "RatingScaleReduction" 

	version("1.4", md5="40bfa7b9667521a5495cb72ea8651b1f")

	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
