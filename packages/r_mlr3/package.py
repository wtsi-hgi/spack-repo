# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3(RPackage):
	"""Machine Learning in R - Next Generation

	Efficient, object-oriented programming on the
    building blocks of machine learning. Provides 'R6' objects for tasks,
    learners, resamplings, and measures. The package is geared towards
    scalability and larger datasets by supporting parallelization and
    out-of-memory data-backends like databases. While 'mlr3' focuses on
    the core computational operations, add-on packages provide additional
    functionality.
	"""
	
	homepage = "https://mlr3.mlr-org.com"
	cran = "mlr3" 

	version("0.18.0", md5="53a1efda2c582c0a1fb6ccbcd562784f", url="https://cran.r-project.org/src/contrib/mlr3_0.18.0.tar.gz")
	version("0.17.2", md5="e8bf4edf11e12f7c0101d3f46e8a02b8", url="https://cran.r-project.org/src/contrib/mlr3_0.17.2.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.15:", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply@1.5:", type=("build", "run"))
	depends_on("r-lgr@0.3.4:", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-mlr3measures@0.4.1:", type=("build", "run"))
	depends_on("r-mlr3misc@0.14:", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-palmerpenguins", type=("build", "run"))
	depends_on("r-paradox@0.10:", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
