# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFertnet(RPackage):
	"""Process Data from the Social Networks and Fertility Survey

	Processes data from The Social Networks and Fertility Survey,
    downloaded from <https://dataarchive.lissdata.nl>, including correcting 
    respondent errors and transforming network data into network objects to
    facilitate analyses and visualisation.
	"""
	
	homepage = "https://github.com/gertstulp/FertNet"
	cran = "FertNet" 

	version("0.1.2", md5="03bab1ffe2aa5b124ea5667d4fbb1a27")

	depends_on("r-haven@2.5.1:", type=("build", "run"))
