# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwarm(RPackage):
	"""Processing Collective Movement Data

	Function library for processing collective movement data (e.g. fish
    schools, ungulate herds, baboon troops) collected from GPS trackers or 
    computer vision tracking software. 
	"""
	
	homepage = "https://swarm-lab.github.io/swaRm/"
	cran = "swaRm" 

	version("0.6.0", md5="017d22c1cba93933446f24b773729f83")

	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
