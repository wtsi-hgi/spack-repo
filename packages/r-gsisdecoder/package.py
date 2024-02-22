# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsisdecoder(RPackage):
	"""High Efficient Functions to Decode NFL Player IDs

	A set of high efficient functions to decode identifiers of National 
  Football League players.
	"""
	
	homepage = "https://github.com/mrcaseb/gsisdecoder"
	cran = "gsisdecoder" 

	version("0.0.1", md5="591e3e8c745a3fb7716a82c2de734fb9")

	depends_on("r-rcpp", type=("build", "run"))
