# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3tuningspaces(RPackage):
	"""Search Spaces for 'mlr3'

	Collection of search spaces for hyperparameter optimization in the
  'mlr3' ecosystem. It features ready-to-use search spaces for many popular
  machine learning algorithms. The search spaces are from scientific articles
  and work for a wide range of data sets.
	"""
	
	homepage = "https://mlr3tuningspaces.mlr-org.com"
	cran = "mlr3tuningspaces" 

	version("0.5.0", md5="6a416ed5061be3bcf7edf5ff92996191")
	version("0.4.0", md5="aa5a1b5037690bd37e232da89b62a25e")

	depends_on("r-mlr3tuning@0.15:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-mlr3@0.11:", type=("build", "run"))
	depends_on("r-mlr3misc@0.11:", type=("build", "run"))
	depends_on("r-paradox@0.7.1:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
