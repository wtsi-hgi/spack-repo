# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHybridts(RPackage):
	"""Hybrid Time Series Forecasting Using Error Remodeling Approach

	Method and tool for generating hybrid time series forecasts using
        an error remodeling approach. These forecasting approaches utilize a recursive 
        technique for modeling the linearity of the series using a linear method 
        (e.g., ARIMA, Theta, etc.) and then models (forecasts) the residuals of the linear forecaster
        using non-linear neural networks (e.g., ANN, ARNN, etc.). The hybrid architectures comprise three steps: 
        firstly, the linear patterns of the series are forecasted which are followed by an error re-modeling step, 
        and finally, the forecasts from both the steps are combined to produce the final output. This method additionally 
        provides the confidence intervals as needed. Ten different models can be implemented using this package.
        This package generates different types of hybrid error correction models for time series forecasting 
        based on the algorithms by Zhang. (2003), Chakraborty et al. (2019), Chakraborty et al. (2020), 
        Bhattacharyya et al. (2021), Chakraborty et al. (2022), and Bhattacharyya et al. (2022)
        <doi:10.1016/S0925-2312(01)00702-0> <doi:10.1016/j.physa.2019.121266> 
        <doi:10.1016/j.chaos.2020.109850> <doi:10.1109/IJCNN52387.2021.9533747> 
        <doi:10.1007/978-3-030-72834-2_29> <doi:10.1007/s11071-021-07099-3>.
	"""
	
	cran = "hybridts" 

	version("0.1.0", md5="62a58a489d6bce950b6033ef24eccf53")

	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
	depends_on("r-waveletarima", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
