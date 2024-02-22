# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingdatacrt(RPackage):
	"""Sampling Data Within Different Study Designs for Cluster
Randomized Trials

	Package provides the possibility to sampling complete datasets 
  from a normal distribution to simulate cluster randomized trails for different study designs. 
	"""
	
	cran = "samplingDataCRT" 

	version("1.0", md5="5a5854b8e7eb592afed6b4f1ed6d5f2f")

	depends_on("r-mvtnorm", type=("build", "run"))
