# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntensitynet(RPackage):
	"""Intensity Analysis of Spatial Point Patterns on Complex Networks

	Tools to analyze point patterns in space occurring over planar network structures derived from graph-related intensity measures for undirected, directed, and mixed networks. 
    This package is based on the following research: Eckardt and Mateu (2018) <doi:10.1080/10618600.2017.1391695>. Eckardt and Mateu (2021) <doi:10.1007/s11749-020-00720-4>.
	"""
	
	cran = "intensitynet" 

	version("1.4.0", md5="629a120d3dd2ee06548a3ed0e14a02d3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-igraph@1.2.5:", type=("build", "run"))
	depends_on("r-intergraph@2.0.2:", type=("build", "run"))
	depends_on("r-matrix@1.5.1:", type=("build", "run"))
	depends_on("r-sna@2.6:", type=("build", "run"))
	depends_on("r-spatstat-geom@2.3.1:", type=("build", "run"))
	depends_on("r-spdep@1.2.1:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
