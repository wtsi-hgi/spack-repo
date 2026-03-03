# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytosimplex(RPackage):
	"""Simplex Visualization of Cell Fate Similarity in Single-Cell
Data

	Create simplex plots to visualize the similarity between 
    single-cells and selected clusters in a 1-/2-/3-simplex space.
    Velocity information can be added as an additional layer. 
    See Liu J, Wang Y et al (2023) <doi:10.1101/2023.12.07.570655> for more details.
	"""
	
	homepage = "https://welch-lab.github.io/CytoSimplex/"
	cran = "CytoSimplex" 

	version("0.1.1", md5="722f4f56e1f121aed3a3ef0a2f240722")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
