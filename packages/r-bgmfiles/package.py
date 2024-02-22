# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgmfiles(RPackage):
	"""Example BGM Files for the Atlantis Ecosystem Model

	A collection of box-geometry model (BGM) files for the Atlantis 
    ecosystem model. Atlantis is a deterministic, biogeochemical, 
    whole-of-ecosystem model (see <http://atlantis.cmar.csiro.au/> for more information).
	"""
	
	homepage = "https://github.com/AustralianAntarcticDivision/bgmfiles/"
	cran = "bgmfiles" 

	version("0.0.6", md5="4ded3c1728dd23a186686d757ff858ab")

