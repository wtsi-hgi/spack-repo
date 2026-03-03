# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReqs(RPackage):
	"""R/EQS Interface

	Contains the function run.eqs() which calls an EQS script file, executes the EQS estimation, and, finally, imports the results as R objects. These two steps can be performed separately: call.eqs() calls and executes EQS, whereas read.eqs() imports existing EQS outputs as objects into R. It requires EQS 6.2 (build 98 or higher).
	"""
	
	cran = "REQS" 

	version("0.8-13", md5="e5c245e838e0f0e5e893e3c4fdf5ae43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
