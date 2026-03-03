# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresens(RPackage):
	"""Interface for PreSens Fiber Optic Data

	Makes output files from select PreSens Fiber Optic Oxygen
    Transmitters easier to work with in R. See <http://www.presens.de> for more
    information about PreSens (Precision Sensing GmbH). Note: this package is
    neither created nor maintained by PreSens.
	"""
	
	cran = "presens" 

	version("2.1.0", md5="8ee8ebda20a5a98670fc5b3275b1f291")

	depends_on("r-marelac@2.1.4:", type=("build", "run"))
	depends_on("r-measurements", type=("build", "run"))
