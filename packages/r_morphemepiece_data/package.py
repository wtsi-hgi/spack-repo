# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorphemepieceData(RPackage):
	"""Data for Morpheme Tokenization

	Provides data about morphemes, the smallest units of meaning in a 
    language.
	"""
	
	homepage = "https://github.com/macmillancontentscience/morphemepiece.data"
	cran = "morphemepiece.data" 

	version("1.2.0", md5="56cba8672eecd54cb41b9bd180196cd1")

	depends_on("r@3.5:", type=("build", "run"))
