# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RFontbitstreamvera(RPackage):
	"""Fonts with 'Bitstream Vera Fonts' License

	Provides fonts licensed under the 'Bitstream Vera Fonts'
    license for the 'fontquiver' package.
	"""
	
	cran = "fontBitstreamVera" 

	version("0.1.1", md5="c32821c06d909336ace68f2df3d8710e")

	depends_on("r@3.0.0:", type=("build", "run"))

