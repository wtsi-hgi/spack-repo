# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrewAwsBatch(RPackage):
	"""A Crew Launcher Plugin for AWS Batch

	In computationally demanding analysis projects,
  statisticians and data scientists asynchronously
  deploy long-running tasks to distributed systems,
  ranging from traditional clusters to cloud services.
  The 'crew.aws.batch' package extends the 'mirai'-powered
  'crew' package with a worker launcher plugin for AWS Batch.
  Inspiration also comes from packages 'mirai' by Gao (2023)
  <https://github.com/shikokuchuo/mirai>,
  'future' by Bengtsson (2021) <doi:10.32614/RJ-2021-048>,
  'rrq' by FitzJohn and Ashton (2023) <https://github.com/mrc-ide/rrq>,
  'clustermq' by Schubert (2019) <doi:10.1093/bioinformatics/btz284>),
  and 'batchtools' by Lang, Bischl, and Surmann (2017).
  <doi:10.21105/joss.00135>.
	"""
	
	homepage = "https://wlandau.github.io/crew.aws.batch/"
	cran = "crew.aws.batch" 

	version("0.0.5", md5="d54a9a43f0171e18017f7ba8350cabd7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-crew@0.8:", type=("build", "run"))
	depends_on("r-paws-common@0.7:", type=("build", "run"))
	depends_on("r-paws-compute", type=("build", "run"))
	depends_on("r-paws-management", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
