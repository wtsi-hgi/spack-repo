# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRespiranalyzer(RPackage):
	"""Analysis Functions of Respiratory Data

	Provides functions for the complete analysis of respiratory data. Consists of a set of functions that allow to preprocessing respiratory data,  calculate both regular statistics and nonlinear statistics, conduct group comparison and visualize the results. Especially, Power Spectral Density ('PSD') (A. Eke (2000) <doi:10.1007/s004249900135>), 'MultiScale Entropy(MSE)' ('Madalena Costa(2002)' <doi:10.1103/PhysRevLett.89.068102>) and 'MultiFractal Detrended Fluctuation Analysis(MFDFA)' ('Jan W.Kantelhardt' (2002) <doi:10.1016/S0378-4371(02)01383-3>) were applied for the analysis of respiratory data. 
	"""
	
	cran = "RespirAnalyzer" 

	version("1.0.2", md5="a5ff50c12dcab8f68fabb6568b25d362")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
