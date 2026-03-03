# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaker(RPackage):
	"""Easy Spatial Microsimulation (Raking) in R

	Functions for performing spatial microsimulation ('raking')
    in R.
	"""
	
	homepage = "https://philmikejones.github.io/rakeR/"
	cran = "rakeR" 

	version("0.2.1", md5="987cb7204b406f4e26ca469b256a2e60")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ipfp", type=("build", "run"))
	depends_on("r-wrswor", type=("build", "run"))
