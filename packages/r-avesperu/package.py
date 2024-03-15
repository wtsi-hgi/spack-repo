# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvesperu(RPackage):
	"""Access to the List of Birds Species of Peru

	Allows access to the data found in the species list featured in the renowned 'List of the Birds of Peru' Plenge, M. A. (2023) <https://sites.google.com/site/boletinunop/checklist>. This publication stands as one of Peru's most comprehensive reviews of bird diversity. The dataset incorporates detailed species accounts and has been meticulously structured for effortless utilization within the R environment.
	"""
	
	homepage = "https://github.com/PaulESantos/avesperu"
	cran = "avesperu" 

	version("0.0.2", md5="146b7d92e1e8441d1dcaff71ce5ab163")

	depends_on("r@2.10:", type=("build", "run"))
