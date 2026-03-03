# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLisreltor(RPackage):
	"""Import Output from LISREL into R

	This is an unofficial package aimed at automating the import of LISREL output in R. 
				This package or its maintainer is not in any way affiliated with the creators of LISREL and SSI, Inc.
	"""
	
	cran = "lisrelToR" 

	version("0.3", md5="23515b702dfcfbf8e2b1284f2d908cda")

	depends_on("r@2.15:", type=("build", "run"))
