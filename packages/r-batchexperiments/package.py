# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchexperiments(RPackage):
	"""Statistical Experiments on Batch Computing Clusters

	Extends the BatchJobs package to run statistical experiments on
    batch computing clusters. For further details see the project web page.
	"""
	
	homepage = "https://github.com/tudo-r/BatchExperiments"
	cran = "BatchExperiments" 

	version("1.4.3", md5="1650314dae3793415cdef17f0998086c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-batchjobs@1.7:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-bbmisc@1.11:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite@2:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
