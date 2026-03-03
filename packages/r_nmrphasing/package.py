# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmrphasing(RPackage):
	"""Phase Error Correction and Baseline Correction for One
Dimensional ('1D') 'NMR' Data

	There are three distinct approaches for phase error correction, they are: a single linear model with a choice of optimization functions, multiple linear models with optimization function choices and a shrinkage-based method. The methodology is based on our new algorithms and various references (Binczyk et al. (2015) <doi:10.1186/1475-925X-14-S2-S5>,Chen et al. (2002) <doi:10.1016/S1090-7807(02)00069-1>, de Brouwer (2009) <doi:10.1016/j.jmr.2009.09.017>, Džakula (2000) <doi:10.1006/jmre.2000.2123>, Ernst (1969) <doi:10.1016/0022-2364(69)90003-1>, Liland et al. (2010) <doi:10.1366/000370210792434350>).
	"""
	
	cran = "NMRphasing" 

	version("1.0.4", md5="70a6bba53dcc2dcb626af1e1cbf97c5d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-baseline", type=("build", "run"))
	depends_on("r-massspecwavelet", type=("build", "run"))
