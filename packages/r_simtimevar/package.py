# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimtimevar(RPackage):
	"""Simulate Longitudinal Dataset with Time-Varying Correlated
Covariates

	Flexibly simulates a dataset with time-varying covariates with user-specified exchangeable correlation structures across and within clusters. Covariates can be normal or binary and can be static within a cluster or time-varying. Time-varying normal variables can optionally have linear trajectories within each cluster. See ?make_one_dataset for the main wrapper function. See Montez-Rath et al. <arXiv:1709.10074> for methodological details. 
	"""
	
	cran = "SimTimeVar" 

	version("1.0.0", md5="27cd421fad61a9e429df95ff0633e4af")

	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-icc", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
