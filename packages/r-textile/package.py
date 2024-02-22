# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextile(RPackage):
	"""Textile Images

	Contains real images of the same textile material 
    with/without local defects, which were used in 
    Bui and Apley (2018) <doi:10.1080/00401706.2017.1302362>.
	"""
	
	cran = "textile" 

	version("0.1.4", md5="b6a61bd4628b96228aee215b067d4c15")

	depends_on("r@4:", type=("build", "run"))
