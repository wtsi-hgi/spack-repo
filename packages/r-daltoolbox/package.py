# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaltoolbox(RPackage):
	"""Leveraging Experiment Lines to Data Analytics

	The natural increase in the complexity of current research experiments and data demands better tools to enhance productivity in Data Analytics. The package is a framework designed to address the modern challenges in data analytics workflows. The package is inspired by Experiment Line concepts. It aims to provide seamless support for users in developing their data mining workflows by offering a uniform data model and method API. It enables the integration of various data mining activities, including data preprocessing, classification, regression, clustering, and time series prediction. It also offers options for hyper-parameter tuning and supports integration with existing libraries and languages. Overall, the package provides researchers with a comprehensive set of functionalities for data science, promoting ease of use, extensibility, and integration with various tools and libraries. Information on Experiment Line is based on Ogasawara et al. (2009) <doi:10.1007/978-3-642-02279-1_20>.
	"""
	
	homepage = "https://github.com/cefet-rj-dal/daltoolbox"
	cran = "daltoolbox" 

	version("1.0.727", md5="400e98f3adeb7df485f634cb38283071")
	version("1.0.767", md5="6ace48725ae8b6f0699c2d523d9bdb61")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-elmnnrcpp", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
