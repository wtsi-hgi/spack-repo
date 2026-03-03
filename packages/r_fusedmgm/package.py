# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFusedmgm(RPackage):
	"""Implementation of Fused MGM to Infer 2-Class Networks

	Implementation of fused Markov graphical model (FMGM; Park and Won, 2022). The functions include building mixed graphical model (MGM) objects from data, inference of networks using FMGM, stable edge-specific penalty selection (StEPS) for the determination of penalization parameters, and the visualization. For details, please refer to Park and Won (2022) <arXiv:2208.14959>.
	"""
	
	cran = "fusedMGM" 

	version("0.1.0.1", md5="c4579796e6f7e2d7471cb290931906e3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
