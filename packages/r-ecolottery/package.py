# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolottery(RPackage):
	"""Coalescent-Based Simulation of Ecological Communities

	Coalescent-Based Simulation of Ecological Communities as proposed
    by Munoz et al. (2017) <doi:10.13140/RG.2.2.31737.26728>. The package includes
    a tool for estimating parameters of community assembly by using Approximate 
    Bayesian Computation.
	"""
	
	homepage = "https://github.com/frmunoz/ecolottery"
	cran = "ecolottery" 

	version("1.0.0", md5="7ad215422152f5e4f89ffbb141eba587")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-abc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
