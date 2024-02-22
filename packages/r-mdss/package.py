# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdss(RPackage):
	"""Modeling Human Dentin Serial Sectioning

	Modeling microstructures of
	human tooth dentin and
	horizontal serial-sectioning of the dentin.
	Corresponding age range of dentin serial sections,
	that is used in stable isotope analyses,
	can be calculated by using this package.
	"""
	
	cran = "MDSS" 

	version("1.0-1", md5="ec23b8e3484c0e08cdc7cd6608f6a96a")

