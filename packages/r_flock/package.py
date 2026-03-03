# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlock(RPackage):
	"""Process Synchronization Using File Locks

	Implements synchronization between R processes (spawned by using the "parallel" package for instance) using file locks. Supports both exclusive and shared locking.
	"""
	
	cran = "flock" 

	version("0.7", md5="479bc5ce265db1f6957cd381d246ed9f")

	depends_on("r-rcpp", type=("build", "run"))
