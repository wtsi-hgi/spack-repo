# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListcompr(RPackage):
	"""List Comprehension for R

	Syntactic shortcuts for creating synthetic lists, vectors, 
    data frames, and matrices using list comprehension.
	"""
	
	homepage = "https://github.com/patrickroocks/listcompr"
	cran = "listcompr" 

	version("0.4.0", md5="866f398e95415e252573fbf881ab7d72")

	depends_on("r@3.1.2:", type=("build", "run"))
