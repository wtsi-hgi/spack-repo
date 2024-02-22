# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchjobs(RPackage):
	"""Batch Computing with R

	Provides Map, Reduce and Filter variants to generate jobs on batch
    computing systems like PBS/Torque, LSF, SLURM and Sun Grid Engine.
    Multicore and SSH systems are also supported. For further details see the
    project web page.
	"""
	
	homepage = "https://github.com/tudo-r/BatchJobs"
	cran = "BatchJobs" 

	version("1.9", md5="68193be1ce553100d2a97c960cf14c84")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bbmisc@1.9:", type=("build", "run"))
	depends_on("r-backports@1.1.1:", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-checkmate@1.8:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rsqlite@1.0.9011:", type=("build", "run"))
	depends_on("r-sendmailr", type=("build", "run"))
	depends_on("r-stringi@0.4.1:", type=("build", "run"))
