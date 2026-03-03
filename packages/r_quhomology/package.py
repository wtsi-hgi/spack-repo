# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuhomology(RPackage):
	"""Calculation of Homology of Quandles, Racks, Biquandles and
Biracks

	Calculates the Quandle, Rack and Degenerate Homology groups of
    Racks and Biracks (as well as Quandles and Biquandles). In addition, a test is
    provided to ascertain if a given set with one or two given functions is indeed a
    biquandle or not.
	"""
	
	cran = "quhomology" 

	version("1.1.1", md5="823bdcb6091b1933ffadacfc10c38509")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
