# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrewCluster(RPackage):
	"""Crew Launcher Plugins for Traditional High-Performance Computing
Clusters

	In computationally demanding analysis projects,
  statisticians and data scientists asynchronously
  deploy long-running tasks to distributed systems,
  ranging from traditional clusters to cloud services.
  The 'crew.cluster' package extends the 'mirai'-powered
  'crew' package with worker launcher plugins for traditional
  high-performance computing systems.
  Inspiration also comes from packages 'mirai' by Gao (2023)
  <https://github.com/shikokuchuo/mirai>,
  'future' by Bengtsson (2021) <doi:10.32614/RJ-2021-048>,
  'rrq' by FitzJohn and Ashton (2023) <https://github.com/mrc-ide/rrq>,
  'clustermq' by Schubert (2019) <doi:10.1093/bioinformatics/btz284>),
  and 'batchtools' by Lang, Bischl, and Surmann (2017).
  <doi:10.21105/joss.00135>.
	"""
	
	homepage = "https://wlandau.github.io/crew.cluster/"
	cran = "crew.cluster" 

	version("0.3.0", md5="b4d2364a28dc0579f508997ea2a49882")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crew@0.8:", type=("build", "run"))
	depends_on("r-ps", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
