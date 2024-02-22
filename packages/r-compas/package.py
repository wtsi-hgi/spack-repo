# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompas(RPackage):
	"""Conformational Manipulations of Protein Atomic Structures

	Manipulate and analyze 3-D structural geometry of Protein Data Bank (PDB) files.
	"""
	
	cran = "compas" 

	version("0.1.1", md5="fe55be44c0b97cdbad807d5fbe587429")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bio3d", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
