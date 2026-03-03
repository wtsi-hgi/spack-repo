# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazytrade(RPackage):
	"""Learn Computer and Data Science using Algorithmic Trading

	Provide sets of functions and methods to learn and practice data science using idea of algorithmic trading.
    Main goal is to process information within "Decision Support System" to come up with analysis or predictions.
    There are several utilities such as dynamic and adaptive risk management using reinforcement learning
    and even functions to generate predictions of price changes using pattern recognition deep regression learning.
    Summary of Methods used: Awesome H2O tutorials: <https://github.com/h2oai/awesome-h2o>, 
    Market Type research of Van Tharp Institute: <https://www.vantharp.com/>,
    Reinforcement Learning R package: <https://CRAN.R-project.org/package=ReinforcementLearning>.
	"""
	
	homepage = "https://vladdsm.github.io/myblog_attempt/topics/lazy%20trading/"
	cran = "lazytrade" 

	version("0.5.3", md5="e406870c388448d347c6d4ee19a9f958")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-h2o", type=("build", "run"))
	depends_on("r-reinforcementlearning", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
