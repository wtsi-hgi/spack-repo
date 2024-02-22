# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeltimeEnsemble(RPackage):
	"""Ensemble Algorithms for Time Series Forecasting with Modeltime

	
    A 'modeltime' extension that implements time series ensemble forecasting methods including model averaging, 
    weighted averaging, and stacking. These techniques are popular methods 
    to improve forecast accuracy and stability. Refer to papers such as 
    "Machine-Learning Models for Sales Time Series Forecasting" Pavlyshenko, B.M. (2019) <doi:10.3390>.
	"""
	
	homepage = "https://github.com/business-science/modeltime.ensemble"
	cran = "modeltime.ensemble" 

	version("1.0.3", md5="f30831201cacae974084c8ae959ea9aa")

	depends_on("r-modeltime@1.2.3:", type=("build", "run"))
	depends_on("r-modeltime-resample@0.2.1:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tune@0.1.2:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
	depends_on("r-workflows@0.2.1:", type=("build", "run"))
	depends_on("r-parsnip@0.1.6:", type=("build", "run"))
	depends_on("r-recipes@0.1.15:", type=("build", "run"))
	depends_on("r-timetk@2.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
