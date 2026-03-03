# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFavnums(RPackage):
	"""A Dataset of Favourite Numbers

	A dataset of favourite numbers, selected from an online poll of over 30,000 people by Alex Bellos
             (http://pages.bloomsbury.com/favouritenumber).
	"""
	
	cran = "favnums" 

	version("1.0.0", md5="dfe905b4411526fa536f7e97aaa3c744")

	depends_on("r@2.10:", type=("build", "run"))
