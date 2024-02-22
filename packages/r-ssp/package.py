# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsp(RPackage):
	"""Simulated Sampling Procedure for Community Ecology

	Simulation-based sampling protocol (SSP) is an R package design to estimate sampling effort in studies of
    ecological communities based on the definition of pseudo-multivariate standard error (MultSE) (Anderson & Santana-Garcon, 2015) <doi:10.1111/ele.12385> and simulation
    of ecological data. The theoretical background is described in Guerra-Castro et al. (2020) <doi:10.1101/2020.03.19.996991>.
	"""
	
	homepage = "https://github.com/edlinguerra/SSP"
	cran = "SSP" 

	version("1.0.1", md5="f942144043da0daa39baedabefa158f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
