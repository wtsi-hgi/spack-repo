# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROppti(RPackage):
	"""Outlier Protein and Phosphosite Target Identifier

	The aim of oppti is to analyze protein (and phosphosite) expressions to find outlying markers for each sample in the given cohort(s) for the discovery of personalized actionable targets.
	"""
	
	homepage = "https://github.com/Huang-lab/oppti"
	bioc = "oppti"

	version("1.22.0", commit="99f68b48655a35c9a6a8126b53eaa69236652087")
	version("1.16.0", commit="7684319d2c7150c1ef258eefd7879c7554f612d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
