# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REngrexpt(RPackage):
	"""Data sets from "Introductory Statistics for Engineering
Experimentation"

	Datasets from Nelson, Coffin and Copeland "Introductory
        Statistics for Engineering Experimentation" (Elsevier, 2003)
        with sample code.
	"""
	
	cran = "EngrExpt" 

	version("0.1-8", md5="b77ca7e21c77365626a244498eb495ac")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
