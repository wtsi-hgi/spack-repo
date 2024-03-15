# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmeffects(RPackage):
	"""Model-Agnostic Interpretations with Forward Marginal Effects

	Create local, regional, and global explanations for any machine learning model with forward marginal effects. You provide a model and data, and 'fmeffects' computes feature effects. The package is based on the theory in: C. A. Scholbeck, G. Casalicchio, C. Molnar, B. Bischl, and C. Heumann (2022) <arXiv:2201.08837>.
	"""
	
	homepage = "https://holgstr.github.io/fmeffects/"
	cran = "fmeffects" 

	version("0.1.2", md5="c62bb9f9b2a7000c6119411425b8411d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-ggparty", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
