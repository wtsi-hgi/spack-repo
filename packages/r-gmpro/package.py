# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmpro(RPackage):
	"""Graph Matching with Degree Profiles

	Functions for graph matching via nodes' degree profiles are provided in this package. The models we can handle include Erdos-Renyi random graphs and stochastic block models(SBM). More details are in the reference paper: Yaofang Hu, Wanjie Wang and Yi Yu (2020) <arXiv:2006.03284>.
	"""
	
	homepage = "https://arxiv.org/abs/2006.03284"
	cran = "GMPro" 

	version("0.1.0", md5="f59ce50bb27c062477443ff80bb4d0b7")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
