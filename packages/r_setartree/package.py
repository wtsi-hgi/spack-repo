# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSetartree(RPackage):
	"""SETAR-Tree - A Novel and Accurate Tree Algorithm for Global Time
Series Forecasting

	The implementation of a forecasting-specific tree-based model that is in particular suitable for global time series forecasting, as proposed in Godahewa et al. (2022) <arXiv:2211.08661v1>. The model uses the concept of Self Exciting Threshold Autoregressive (SETAR) models to define the node splits and thus, the model is named SETAR-Tree. The SETAR-Tree uses some time-series-specific splitting and stopping procedures. It trains global pooled regression models in the leaves allowing the models to learn cross-series information. The depth of the tree is controlled by conducting a statistical linearity test as well as measuring the error reduction percentage at each node split. Thus, the SETAR-Tree requires minimal external hyperparameter tuning and provides competitive results under its default configuration. A forest is developed by extending the SETAR-Tree. The SETAR-Forest combines the forecasts provided by a collection of diverse SETAR-Trees during the forecasting process. 
	"""
	
	homepage = "https://github.com/rakshitha123/setartree"
	cran = "setartree" 

	version("0.2.1", md5="2859d0e0ae02cdb580de4c3c67b567f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
