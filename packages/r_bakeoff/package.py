# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBakeoff(RPackage):
	"""Data from "The Great British Bake Off"

	Data about the bakers, challenges, and ratings 
    for "The Great British Bake Off", 
    from Wikipedia <https://en.wikipedia.org/wiki/The_Great_British_Bake_Off>.
	"""
	
	homepage = "https://bakeoff.netlify.app/"
	cran = "bakeoff" 

	version("0.2.0", md5="fa961733bc689c88d10c7856a2adf1af")

	depends_on("r@2.10:", type=("build", "run"))
