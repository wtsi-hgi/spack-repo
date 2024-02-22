# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsensembler(RPackage):
	"""Dynamic Ensembles for Time Series Forecasting

	A framework for dynamically combining forecasting models for time series forecasting predictive tasks. It leverages machine learning models from other packages to automatically combine expert advice using metalearning and other state-of-the-art forecasting combination approaches. The predictive methods receive a data matrix as input, representing an embedded time series, and return a predictive ensemble model. The ensemble use generic functions 'predict()' and 'forecast()' to forecast future values of the time series. Moreover, an ensemble can be updated using methods, such as 'update_weights()' or 'update_base_models()'. A complete description of the methods can be found in: Cerqueira, V., Torgo, L., Pinto, F., and Soares, C. "Arbitrated Ensemble for Time Series Forecasting." to appear at: Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Springer International Publishing, 2017; and Cerqueira, V., Torgo, L., and Soares, C.: "Arbitrated Ensemble for Solar Radiation Forecasting." International Work-Conference on Artificial Neural Networks. Springer, 2017 <doi:10.1007/978-3-319-59153-7_62>.
	"""
	
	homepage = "https://github.com/vcerqueira/tsensembler"
	cran = "tsensembler" 

	version("0.1.0", md5="44ed50253fe25babb726a480b341d063")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-cubist", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-monmlp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
