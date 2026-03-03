# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdbook(RPackage):
	"""Support Functions and Data for "Ecological Models and Data"

	Auxiliary functions and data sets for "Ecological Models and Data", a book presenting maximum likelihood estimation and related topics for ecologists (ISBN 978-0-691-12522-0).
	"""
	
	homepage = "https://www.math.mcmaster.ca/bolker/emdbook"
	cran = "emdbook" 

	version("1.3.13", md5="fcd352167d96a8bc174a1a3cf32b9bec")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
