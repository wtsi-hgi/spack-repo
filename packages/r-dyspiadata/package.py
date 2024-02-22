# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyspiadata(RPackage):
	"""Background and Pathway Data Used in 'DysPIA'

	This dataset includes Background and Pathway data used in package 'DysPIA'.
	"""
	
	cran = "DysPIAData" 

	version("0.1.2", md5="ba566e88b3585f725a5bddf7fb3df4cb")

	depends_on("r@3.5:", type=("build", "run"))
