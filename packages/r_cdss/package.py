# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdss(RPackage):
	"""Course-Dependent Skill Structures

	Deriving skill structures from skill assignment 
    data for courses (sets of learning objects).
	"""
	
	cran = "CDSS" 

	version("0.2-0", md5="e2195d26d63966e07c8733de3175aeb2")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-readods@2:", type=("build", "run"))
	depends_on("r-openxlsx@4.2:", type=("build", "run"))
