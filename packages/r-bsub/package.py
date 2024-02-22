# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsub(RPackage):
	"""Submitter and Monitor of the 'LSF Cluster'

	It submits R code/R scripts/shell commands to 'LSF cluster' 
  (<https://en.wikipedia.org/wiki/Platform_LSF>, the 'bsub' system) without 
  leaving R. There is also an interactive 'shiny' app for monitoring the job status.
	"""
	
	homepage = "https://github.com/jokergoo/bsub"
	cran = "bsub" 

	version("1.1.0", md5="cf456a7f2ae00ec7e909be7d3faa10bc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-globaloptions@0.1.1:", type=("build", "run"))
	depends_on("r-getoptlong@0.1.8:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
