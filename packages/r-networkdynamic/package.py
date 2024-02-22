# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkdynamic(RPackage):
	"""Dynamic Extensions for Network Objects

	Simple interface routines to facilitate the handling of network objects with complex intertemporal data. This is a part of the "statnet" suite of packages for network analysis.
	"""
	
	homepage = "https://statnet.org/"
	cran = "networkDynamic" 

	version("0.11.4", md5="01cf934ffb0fd9f393f13e432099d45b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-networklite", type=("build", "run"))
