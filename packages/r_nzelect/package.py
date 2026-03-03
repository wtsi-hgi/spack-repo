# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNzelect(RPackage):
	"""New Zealand Election Data

	Convenient access to New Zealand election
    results by voting place.  Voting places have been matched to Regional Council,
    Territorial Authority, and Area Unit, to facilitate matching with additional data.
    Opinion polls since 2002 and some convenience analytical function are also supplied.
	"""
	
	cran = "nzelect" 

	version("0.4.0", md5="9c7ca4d90c9048e37be526115c3b226a")

	depends_on("r@3.1.2:", type=("build", "run"))
