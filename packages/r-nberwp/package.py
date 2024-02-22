# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNberwp(RPackage):
	"""NBER Working Papers

	Catalogue of NBER working papers published between June 1973 and December 2021.
	"""
	
	homepage = "https://github.com/bldavies/nberwp"
	cran = "nberwp" 

	version("1.2.0", md5="2f35708bb60830af0616aa6f3efecb55")

	depends_on("r@2.10:", type=("build", "run"))
