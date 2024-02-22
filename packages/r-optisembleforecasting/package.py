# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptisembleforecasting(RPackage):
	"""Optimization Based Ensemble Forecasting Using MCS Algorithm

	The real-life data is complex in nature. No single model can capture all aspect of complex time series data. In this package, 14 models, namely Recurrent Neural Network (RNN), Gated Recurrent Unit (GRU), Long Short-Term Memory (LSTM), Bidirectional LSTM, Deep LSTM, Artificial Neural Network (ANN), Support Vector Regression (SVR), Random Forest (RF), k-Nearest Neighbour (KNN), XGBoost (XGB), Autoregressive Integrated Moving Average (ARIMA), Error-Trend-Seasonality (ETS) and TBATS models, have been implemented and their accuracy have been checked. An PCA based error index has been proposed to select a group of best models using MCS algorithms. After selecting the models, the forecasts from these models have been ensembled using optimization techniques. This package allows to implement 20 optimization techniques, namely, Artificial Bee Colony (ABC), Ant Lion Optimizer (ALO), Bat Algorithm (BA), Black Hole Optimization Algorithm (BHO), Clonal Selection Algorithm (CLONALG), Cuckoo Search (CS), Cat Swarm Optimization (CSO), Dragonfly Algorithm (DA), Differential Evolution (DE), Firefly Algorithm (FFA), Genetic Algorithm (GA), Gravitational Based Search Algorithm (GBS), Grasshopper Optimisation Algorithm (GOA), Grey Wolf Optimizer (GWO), Harmony Search Algorithm (HS), Krill-Herd Algorithm (KH), Moth Flame Optimizer (MFO), Particle Swarm Optimization (PSO), Sine Cosine Algorithm (SCA), Shuffled Frog Leaping (SFL) and Whale Optimization Algorithm (WOA). This package has been developed using concept of Wang et al. (2022) <doi:10.1016/j.apm.2022.09.004>, Qu et al. (2022) <doi:10.1016/j.eswa.2022.118746> and Kriz (2019) <doi:10.1007/978-3-030-18195-6_21 >.
	"""
	
	cran = "OptiSembleForecasting" 

	version("0.1.0", md5="c2b2156bc81c6b29644cf4ad02504b96")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-mcs", type=("build", "run"))
	depends_on("r-caretforecast", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-metaheuristicopt", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
