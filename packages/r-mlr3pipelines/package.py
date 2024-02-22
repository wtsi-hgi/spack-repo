# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3pipelines(RPackage):
	"""Preprocessing Operators and Pipelines for 'mlr3'

	Dataflow programming toolkit that enriches 'mlr3' with a diverse
  set of pipelining operators ('PipeOps') that can be composed into graphs.
  Operations exist for data preprocessing, model fitting, and ensemble
  learning. Graphs can themselves be treated as 'mlr3' 'Learners' and can
  therefore be resampled, benchmarked, and tuned.
	"""
	
	homepage = "https://mlr3pipelines.mlr-org.com"
	cran = "mlr3pipelines" 

	version("0.5.0-2", md5="c8e6820c8b7d39bcbbd1dde6980c7286")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3@0.6:", type=("build", "run"))
	depends_on("r-mlr3misc@0.9:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
