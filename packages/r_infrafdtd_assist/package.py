# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfrafdtdAssist(RPackage):
	"""IO Help for infraFDTD Model

	Facilitates the generation of input files for infraFDTD and processes snapshot output. infraFDTD is a finite-difference model written by Keehoon Kim for simulating infrasound that considers topography and a 1-D atmosphere (see Kim et al., 2015 <doi:10.1002/2015GL064466>).
	"""
	
	cran = "infraFDTD.assist" 

	version("0.6", md5="cc92950e615d11bee9d7f63b15dbca59")

	depends_on("r-fields", type=("build", "run"))
