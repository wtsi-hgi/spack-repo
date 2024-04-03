# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrew(RPackage):
	"""A Distributed Worker Launcher Framework

	In computationally demanding analysis projects,
  statisticians and data scientists asynchronously
  deploy long-running tasks to distributed systems,
  ranging from traditional clusters to cloud services.
  The 'NNG'-powered 'mirai' R package by Gao (2023)
  <doi:10.5281/zenodo.7912722> is a sleek
  and sophisticated scheduler that
  efficiently processes these intense workloads.
  The 'crew' package extends 'mirai' with a unifying
  interface for third-party worker launchers.
  Inspiration also comes from packages.
  'future' by Bengtsson (2021) <doi:10.32614/RJ-2021-048>,
  'rrq' by FitzJohn and Ashton (2023) <https://github.com/mrc-ide/rrq>,
  'clustermq' by Schubert (2019) <doi:10.1093/bioinformatics/btz284>),
  and 'batchtools' by Lang, Bischel, and Surmann (2017)
  <doi:10.21105/joss.00135>.
	"""
	
	homepage = "https://wlandau.github.io/crew/"
	cran = "crew" 

	version("0.9.0", md5="219f501c0f07c5f172f9cff94b23cd41")
	version("0.9.1", md5="c1a4c790e68478ce65efc84c34d68f28")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-getip", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-mirai@0.12:", type=("build", "run"))
	depends_on("r-nanonext@0.12:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-ps", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
