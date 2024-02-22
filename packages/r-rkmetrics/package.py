# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkmetrics(RPackage):
	"""Hybrid Mortality Estimation

	Hybrid Mortality Modelling (HMM) provides a framework in which mortality around "the accident hump" and at very old ages can be modelled under a single model. The graphics' codes necessary for visualization of the models' output are included here. Specifically, the graphics are based on the assumption that, the mortality rates can be expressed as a function of the area under the curve between the crude mortality rates plots and the tangential transform of the force of mortality.
	"""
	
	cran = "RkMetrics" 

	version("1.3", md5="92c136d5d411c4b5fcdd0a9b75197a43")

	depends_on("r@3.4:", type=("build", "run"))
