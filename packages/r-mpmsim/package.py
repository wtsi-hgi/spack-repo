# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpmsim(RPackage):
	"""Simulation of Matrix Population Models with Defined Life History
Characteristics

	Allows users to simulate matrix population models with
    particular characteristics based on aspects of life history such as
    mortality trajectories and fertility trajectories. Also allows the
    exploration of sampling error due to small sample size.
	"""
	
	homepage = "https://github.com/jonesor/mpmsim"
	cran = "mpmsim" 

	version("2.0.0", md5="182f3e4f442fc2a68304b85c6c90e6b7")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-popbio", type=("build", "run"))
	depends_on("r-popdemo", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rcompadre", type=("build", "run"))
