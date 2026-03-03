# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecom(RPackage):
	"""'Recom' REmoves COMments of Rscript File for you

	Goal of 'recom' package is to remove all the comments of the Rscript file, and to reduce Rscript file size for better performance.
	"""
	
	cran = "recom" 

	version("1.0", md5="0ab45994a0fa48aa2f66d7b505a4165a")

	depends_on("r-rcpp", type=("build", "run"))
