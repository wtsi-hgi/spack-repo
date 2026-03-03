# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkxgb(RPackage):
	"""Interface for 'XGBoost' on 'Apache Spark'

	A 'sparklyr' <https://spark.rstudio.com/> extension that provides an R
  interface for 'XGBoost' <https://github.com/dmlc/xgboost> on 'Apache Spark'. 'XGBoost' is an
  optimized distributed gradient boosting library.
	"""
	
	cran = "sparkxgb" 

	version("0.1.1", md5="3dcfab93d652ab2a834b49fe49ac4123")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-sparklyr@1.3:", type=("build", "run"))
	depends_on("r-forge@0.1.9005:", type=("build", "run"))
