# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfflhd(RPackage):
	"""Sequential Full Factorial-Based Latin Hypercube Design

	Gives design points from a sequential full factorial-based
 Latin hypercube design, as described in Duan, Ankenman, Sanchez,
 and Sanchez (2015, Technometrics,
 <doi:10.1080/00401706.2015.1108233>).
	"""
	
	homepage = "https://github.com/CollinErickson/sFFLHD"
	cran = "sFFLHD" 

	version("0.1.2", md5="d580e69e55baa30c1b7472babcd503e5")

	depends_on("r-doe-base", type=("build", "run"))
	depends_on("r-conf-design", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
