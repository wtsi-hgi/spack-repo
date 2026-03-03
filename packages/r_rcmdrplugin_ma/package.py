# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginMa(RPackage):
	"""Graphical User Interface for Conducting Meta-Analyses in R

	Easy to use interface for conducting meta-analysis in R. This
    package is an Rcmdr-plugin, which allows the user to conduct analyses in a
    menu-driven, graphical user interface environment (e.g., CMA, SPSS). It
    uses recommended procedures as described in The Handbook of Research
    Synthesis and Meta-Analysis (Cooper, Hedges, & Valentine, 2009).
	"""
	
	homepage = "http://acdelre.weebly.com/"
	cran = "RcmdrPlugin.MA" 

	version("0.0-2", md5="64966ff2f744e8f8bfbff24f6da11099")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
	depends_on("r-mad", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
