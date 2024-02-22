# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaewr(RPackage):
	"""Design and Analysis of Experiments with R

	Contains Data frames and functions used in the book "Design and Analysis of Experiments with R", Lawson(2015) ISBN-13:978-1-4398-6813-3.
	"""
	
	cran = "daewr" 

	version("1.2-11", md5="ed0ec58f19b45350ee2ac53af0b4ecff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
