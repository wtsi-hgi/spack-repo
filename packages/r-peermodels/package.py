# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeermodels(RPackage):
	"""Client-Side R API Wrapper for Peer Models Network Model
Repository

	Enables direct cloud access to health care decision models hosted on the PRISM server of the Peer Models Network.
	"""
	
	homepage = "https://www.peermodelsnetwork.com"
	cran = "peermodels" 

	version("0.10.3", md5="c5bb4dbf5a03fc2a7824ab9691417cb0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
