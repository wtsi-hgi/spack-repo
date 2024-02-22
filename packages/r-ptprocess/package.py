# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtprocess(RPackage):
	"""Time Dependent Point Process Modelling

	Fits and analyses time dependent marked point process models with an emphasis on earthquake modelling. For a more detailed introduction to the package, see the topic "PtProcess". A list of recent changes can be found in the topic "Change Log".
	"""
	
	homepage = "https://www.statsresearch.co.nz/dsh/sslib/"
	cran = "PtProcess" 

	version("3.3-16", md5="bc4b8c36cacabbf868eebd26d69b6c09")

