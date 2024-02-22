# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuir(RPackage):
	"""Exploring Data with Tree Data Structures

	A simple tool allowing users to easily and dynamically explore or document a data set using a tree structure.
	"""
	
	homepage = "https://github.com/alforj/muir"
	cran = "muir" 

	version("0.1.0", md5="10541d7168baa109abe459613d7dc971")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-diagrammer@0.6:", type=("build", "run"))
	depends_on("r-dplyr@0.4.1:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
