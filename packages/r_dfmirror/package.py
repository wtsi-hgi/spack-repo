# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfmirror(RPackage):
	"""Simulate a Data Frame Mirroring an Input and Produce Shareable
Simulation Code

	The 'dfmirroR' package allows users to input a data frame, simulate some number of observations based on specified columns of that data frame, and then outputs a string that contains the code to re-create the simulation. The goal is to both provide workable test data sets and provide users with the information they need to set up reproducible examples with team members. This package was created out of a need to share examples in cases where data are private and where a full data frame is not needed for testing or coordinating.
	"""
	
	homepage = "https://github.com/jacobpstein/dfmirroR"
	cran = "dfmirroR" 

	version("2.1.0", md5="b94cdb26a932acf48dbb2556823bd4f4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
