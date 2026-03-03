# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVmdtdnn(RPackage):
	"""VMD Based Time Delay Neural Network Model

	Forecasting univariate time series with Variational Mode Decomposition (VMD) based time delay neural network models.For method details see Konstantin, D.and Dominique, Z. (2014). <doi:10.1109/TSP.2013.2288675>. 
	"""
	
	cran = "vmdTDNN" 

	version("0.1.1", md5="174e326e3d5fc0e0ae2ada8be8e83024")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
	depends_on("r-vmdecomp", type=("build", "run"))
