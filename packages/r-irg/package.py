# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrg(RPackage):
	"""Instantaneous Rate of Green Up

	Fits a double logistic function to NDVI time series and calculates 
             instantaneous rate of green (IRG) according to methods described
             in Bischoff et al. (2012) <doi:10.1086/667590>. 
	"""
	
	homepage = "https://github.com/robitalec/irg"
	cran = "irg" 

	version("0.1.6", md5="a89299788a6d3a7f810b54de83e36c43")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
