# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdota2(RPackage):
	"""An R Steam API Client for Valve's Dota2

	An R API Client for Valve's Dota2. RDota2 can be easily used 
    to connect to the Steam API and retrieve data for Valve's popular video 
    game Dota2. You can find out more about Dota2 at 
    <http://store.steampowered.com/app/570/>.
	"""
	
	homepage = "https://github.com/LyzandeR/RDota2"
	cran = "RDota2" 

	version("0.1.6", md5="6ddf6fe38678395f1cd1702a030e35eb", url="https://cran.r-project.org/src/contrib/RDota2_0.1.6.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
