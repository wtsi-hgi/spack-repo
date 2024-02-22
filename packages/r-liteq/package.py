# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiteq(RPackage):
	"""Lightweight Portable Message Queue Using 'SQLite'

	Temporary and permanent message queues for R. Built on top of
    'SQLite' databases. 'SQLite' provides locking, and makes it possible
    to detect crashed consumers. Crashed jobs can be automatically marked
    as "failed", or put in the queue again, potentially a limited number of times.
	"""
	
	homepage = "https://github.com/r-lib/liteq#readme"
	cran = "liteq" 

	version("1.1.0", md5="cb7db1a625f012026492bc2737c13a43")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
