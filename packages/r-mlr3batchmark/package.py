# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3batchmark(RPackage):
	"""Batch Experiments for 'mlr3'

	Extends the 'mlr3' package with a connector to the package
    'batchtools'. This allows to run large-scale benchmark experiments on
    scheduled high-performance computing clusters.
	"""
	
	homepage = "https:///mlr3batchmark.mlr-org.com"
	cran = "mlr3batchmark" 

	version("0.1.1", md5="4e7b68bc8a0b291c48d8d320c46ca57e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-batchtools@0.9.17:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3@0.17:", type=("build", "run"))
	depends_on("r-mlr3misc", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
