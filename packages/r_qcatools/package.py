# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcatools(RPackage):
	"""Helper Functions for QCA in R

	Helper functions for Qualitative Comparative Analysis: evaluate and
    plot Boolean formulae on fuzzy set score data, apply Boolean operations, compute
    consistency and coverage measures.
	"""
	
	cran = "QCAtools" 

	version("0.2.3", md5="d843c53239c3ec4f0503cc083830e3ac")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.3.1:", type=("build", "run"))
	depends_on("r-directlabels@2013.6.15:", type=("build", "run"))
	depends_on("r-qca@2.5:", type=("build", "run"))
