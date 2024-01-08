# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RTfautograph(RPackage):
	"""Autograph R for 'Tensorflow'

	Translate R control flow expressions into 'Tensorflow' graphs.
	"""
	
	homepage = "https://t-kalinowski.github.io/tfautograph/"
	cran = "tfautograph" 

	version("0.3.2", md5="6079dca33e05c371b979545f2a9d5091")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
