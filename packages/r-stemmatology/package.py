# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStemmatology(RPackage):
	"""Stemmatological Analysis of Textual Traditions

	Explore and analyse the genealogy of textual or musical traditions, from their variants, with various stemmatological methods, mainly the disagreement-based algorithms suggested by Camps and Cafiero (2015) <doi:10.1484/M.LECTIO-EB.5.102565>.
	"""
	
	homepage = "https://github.com/Jean-Baptiste-Camps/stemmatology"
	cran = "stemmatology" 

	version("0.3.2", md5="7eb540752ac925a785e26a04bd0d8435")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
