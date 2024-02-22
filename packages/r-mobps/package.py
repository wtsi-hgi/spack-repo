# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobps(RPackage):
	"""Modular Breeding Program Simulator

	Framework for the simulation framework for the simulation of complex breeding programs and compare their economic and genetic impact. The package is also used as the background simulator for our a web-based interface <http:www.mobps.de>. Associated publication: Pook et al. (2020) <doi:10.1534/g3.120.401193>.
	"""
	
	cran = "MoBPS" 

	version("1.6.64", md5="0ce2edbfc6cc8c4731c71699618a46ec")

	depends_on("r@3:", type=("build", "run"))
