# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigerstats(RPackage):
	"""R Functions for Elementary Statistics

	A collection of data sets and functions that are useful in the
    teaching of statistics at an elementary level to students who may have
    little or no previous experience with the command line.  The functions for
    elementary inferential procedures follow a uniform interface for user
    input.  Some of the functions are instructional applets that can only be
    run on the R Studio integrated development environment with package
    'manipulate' installed.  Other instructional applets are Shiny apps
    that may be run locally. In teaching the package is used alongside of
    package 'mosaic', 'mosaicData' and 'abd', which are therefore listed as
    dependencies.
	"""
	
	cran = "tigerstats" 

	version("0.3.2", md5="342e00e79b1abfed335c18b2c2047e06")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-abd", type=("build", "run"))
	depends_on("r-mosaic", type=("build", "run"))
	depends_on("r-mosaicdata", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-manipulate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
