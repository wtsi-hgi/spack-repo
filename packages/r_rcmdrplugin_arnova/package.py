# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginArnova(RPackage):
	"""R Commander Plug-in for Repeated-Measures ANOVA

	R Commander plug-in for repeated-measures and mixed-design
    ('split-plot') ANOVA.
    It adds a new menu entry for repeated measures that allows
    to deal with up to three within-subject factors and optionally with
    one or several between-subject factors.
    It also provides supplementary options to oneWayAnova() and
    multiWayAnova() functions, such as choice of ANOVA type, display of
    effect sizes and post hoc analysis for multiWayAnova().
	"""
	
	cran = "RcmdrPlugin.aRnova" 

	version("0.0.5", md5="1d3f318e75e9bd54f9b62bb70091520b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
