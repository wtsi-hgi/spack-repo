# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscord(RPackage):
	"""Functions for Discordant Kinship Modeling

	Functions for discordant kinship modeling (and other sibling-based quasi-experimental designs). Currently, the package contains data restructuring functions and functions for generating biometrically informed data for kin pairs.
	"""
	
	homepage = "https://github.com/R-Computing-Lab/discord"
	cran = "discord" 

	version("1.1.0", md5="9fb8cf77a17b439286eb217be72f7f25")

	depends_on("r@2.10:", type=("build", "run"))
