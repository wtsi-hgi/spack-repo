# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnfor(RPackage):
	"""Time Series Forecasting with Neural Networks

	Automatic time series modelling with neural networks. 
    Allows fully automatic, semi-manual or fully manual specification of networks. For details of the
	specification methodology see: (i) Crone and Kourentzes (2010) <doi:10.1016/j.neucom.2010.01.017>;
	and (ii) Kourentzes et al. (2014) <doi:10.1016/j.eswa.2013.12.011>.
	"""
	
	homepage = "https://kourentzes.com/forecasting/2019/01/16/tutorial-for-the-nnfor-r-package/"
	cran = "nnfor" 

	version("0.9.9", md5="72b78da06a75029adf64ff070a300030")

	depends_on("r-generics", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
	depends_on("r-uroot", type=("build", "run"))
