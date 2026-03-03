# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWwgbook(RPackage):
	"""Functions and Datasets for WWGbook

	Book is "Linear Mixed Models: A Practical Guide Using
        Statistical Software" published in 2006 by Chapman Hall / CRC
        Press.
	"""
	
	homepage = "http://www-personal.umich.edu/~bwest/almmussp.html"
	cran = "WWGbook" 

	version("1.0.2", md5="74d29098b346182b70b2c131f1071f1e")

	depends_on("r@1.4.1:", type=("build", "run"))
