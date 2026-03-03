# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXgb2sql(RPackage):
	"""Convert Trained 'XGBoost' Model to SQL Query

	This tool enables in-database scoring of 'XGBoost' models built in R, by translating trained model objects into SQL query. 
  'XGBoost' <https://xgboost.readthedocs.io/en/latest/index.html> provides parallel tree boosting (also known as gradient boosting machine, or GBM) algorithms
  in a highly efficient, flexible and portable way. GBM algorithm is introduced by Friedman (2001) <doi:10.1214/aos/1013203451>, 
  and more details on 'XGBoost' can be found in Chen & Guestrin (2016) <doi:10.1145/2939672.2939785>.
	"""
	
	homepage = "https://github.com/chengjunhou/xgb2sql"
	cran = "xgb2sql" 

	version("0.1.2", md5="4fd4e64405d817e95e4bdb49cf520a70")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xgboost@0.81.0.1:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
