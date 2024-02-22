# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBionetdata(RPackage):
	"""Biological and Chemical Data Networks

	Data Package that includes several examples of chemical and biological data networks, i.e. data graph structured.
	"""
	
	cran = "bionetdata" 

	version("1.1", md5="83e0beb90e9edd11f5d02e4eba4ae757")

	depends_on("r@2.10:", type=("build", "run"))
