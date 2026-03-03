# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishbc(RPackage):
	"""Fishes of British Columbia

	Provides raw and curated data on the codes,
    classification and conservation status of freshwater fishes in British
    Columbia. Marine fishes will be added in a future release.
	"""
	
	homepage = "https://github.com/poissonconsulting/fishbc"
	cran = "fishbc" 

	version("0.2.1", md5="0f102d2afbaffcb38056ca3b78bd20da")

	depends_on("r@3.4:", type=("build", "run"))
