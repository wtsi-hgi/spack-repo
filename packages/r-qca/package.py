# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQca(RPackage):
	"""Qualitative Comparative Analysis

	An extensive set of functions to perform Qualitative Comparative Analysis:
       crisp sets ('csQCA'), temporal ('tQCA'), multi-value ('mvQCA')
       and fuzzy sets ('fsQCA'), using a GUI - graphical user interface.
       'QCA' is a methodology that bridges the qualitative and quantitative
       divide in social science research. It uses a Boolean minimization
       algorithm, resulting in a minimal causal configuration associated
       with a given phenomenon.
	"""
	
	cran = "QCA" 

	version("3.22", md5="1cf3129879bf651141f70865322c4632")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-admisc@0.34:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-declared", type=("build", "run"))
	depends_on("r-venn", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
