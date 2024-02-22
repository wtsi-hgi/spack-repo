# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsar(RPackage):
	"""Introduction to Sports Analytics using R (ISAR) Data

	We provide data sets used in the forthcoming textbook "Introduction to Sports Analytics using R" by Elmore and Urbaczweski (2024). The package currently contains sixteen datasets and should be published in early 2024.  
	"""
	
	homepage = "https://github.com/rtelmore/ISAR"
	cran = "ISAR" 

	version("0.1.12", md5="b8191a01f5db000851d011092dc24f55")

	depends_on("r@2.10:", type=("build", "run"))
