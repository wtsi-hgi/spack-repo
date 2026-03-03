# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdapttest(RPackage):
	"""Adaptive Two-Stage Tests

	The functions defined in this program serve for implementing adaptive
    two-stage tests. Currently, four tests are included: Bauer and Koehne (1994),
    Lehmacher and Wassmer (1999), Vandemeulebroecke (2006), and the horizontal conditional
    error function. User-defined tests can also be implemented. Reference: Vandemeulebroecke,
    An investigation of two-stage tests, Statistica Sinica 2006.
	"""
	
	cran = "adaptTest" 

	version("1.2", md5="ea6bbfe2f0cbadf19e21270d22303e2e")

	depends_on("r-lattice", type=("build", "run"))
