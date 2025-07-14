# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErccdashboard(RPackage):
	"""Assess Differential Gene Expression Experiments with ERCC Controls

	Technical performance metrics for differential gene expression experiments using External RNA Controls Consortium (ERCC) spike-in ratio mixtures.
	"""
	
	homepage = "https://github.com/munrosa/erccdashboard"
	bioc = "erccdashboard"

	version("1.42.0", commit="1164513c353349995ffdbb1646deeaa54c21b66f")
	version("1.36.0", commit="ec57f0e6a8d61d845cdbdd3f2e17fd77d7fe25b3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
