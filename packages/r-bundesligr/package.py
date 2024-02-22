# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBundesligr(RPackage):
	"""All Final Tables of the Bundesliga

	All final tables of Germany's highest football (soccer!) league, the Bundesliga. Contains data from 1964 to 2016.
	"""
	
	homepage = "https://github.com/ottlngr/bundesligR"
	cran = "bundesligR" 

	version("0.1.0", md5="f0512b0d9e567787dd3b74606bdd2733")

	depends_on("r@2.10:", type=("build", "run"))
