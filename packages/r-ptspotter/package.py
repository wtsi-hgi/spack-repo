# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtspotter(RPackage):
	"""Helper Functions for Use with "ProjectTemplate"

	Utility functions produced specifically for (but not limited
    to) working with 'ProjectTemplate' data pipelines. This package helps
    to quickly create and manage sequentially numbered scripts, quickly
    set up logging with 'log4r' and functions to help debug and monitor
    procedures.
	"""
	
	homepage = "https://github.com/r-leyshon/ptspotter"
	cran = "ptspotter" 

	version("1.0.2", md5="6b95b965a83c34e2b873f007c0553281")

	depends_on("r-beepr@1.3:", type=("build", "run"))
	depends_on("r-log4r@0.3.2:", type=("build", "run"))
	depends_on("r-this-path@0.2:", type=("build", "run"))
	depends_on("r-pryr@0.1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
