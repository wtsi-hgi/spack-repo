# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSims(RPackage):
	"""Simulate Data from R or 'JAGS' Code

	Generates data from R or 'JAGS' code for use in simulation
    studies.  The data are returned as an 'nlist::nlists' object and/or
    saved to file as individual '.rds' files.  Parallelization is
    implemented using the 'future' package.  Progress is reported using
    the 'progressr' package.
	"""
	
	cran = "sims" 

	version("0.0.3", md5="5e56a3f95b7932396c951fc939a546de")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-nlist", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
