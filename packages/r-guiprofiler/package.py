# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuiprofiler(RPackage):
	"""Graphical User Interface for Rprof()

	Show graphically the results of profiling R functions by tracking their execution time.
	"""
	
	cran = "GUIProfiler" 

	version("2.0.1", md5="4f76fbc0a9f4d8bf0dd543aab97d7875")

	depends_on("r-nozzle-r1", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-proftools", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
