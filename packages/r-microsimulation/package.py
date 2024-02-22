# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrosimulation(RPackage):
	"""Discrete Event Simulation in R and C++, with Tools for
Cost-Effectiveness Analysis

	Discrete event simulation using both R and C++ (Karlsson et al 2016; <doi:10.1109/eScience.2016.7870915>). The C++ code is adapted from the SSIM library <https://www.inf.usi.ch/carzaniga/ssim/>, allowing for event-oriented simulation. The code includes a SummaryReport class for reporting events and costs by age and other covariates. The C++ code is available as a static library for linking to other packages. A priority queue implementation is given in C++ together with an S3 closure and a reference class implementation. Finally, some tools are provided for cost-effectiveness analysis.
	"""
	
	homepage = "https://github.com/mclements/microsimulation"
	cran = "microsimulation" 

	version("1.4.3", md5="08f7afe175cbaf6a5284293ccdbb50c6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ascii", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
