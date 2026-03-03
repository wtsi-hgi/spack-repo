# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstabledist(RPackage):
	"""The Discrete Stable Distribution Functions

	Probability generating function,  formulae for the probabilities (discrete density) and random generation for discrete stable random variables.
	"""
	
	cran = "dstabledist" 

	version("0.1.0", md5="9ccd064dd78184c814e5787eabcd8159")

	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
