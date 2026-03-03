# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatbasics(RPackage):
	"""Basic Functions to Statistical Methods Course

	Basic statistical methods with some modifications for the course Statistical Methods at Federal University of Bahia (Brazil). All methods in this packages are explained in the text book of Montgomery and Runger (2010) <ISBN: 978-1-119-74635-5>.
	"""
	
	cran = "statBasics" 

	version("0.2.0", md5="0c91d106d8ff76aa11a9d571e562eea2")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
