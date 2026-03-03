# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpdb(RPackage):
	"""Read, Write, Visualize and Manipulate PDB Files

	Provides tools to read, write, visualize Protein Data Bank (PDB) files and
    perform some structural manipulations.
	"""
	
	homepage = "https://github.com/discoleo/Rpdb"
	cran = "Rpdb" 

	version("2.3.4", md5="75e75d9060f8b1eeb747073d6ab4db2a")

	depends_on("r-rgl@1.1.3:", type=("build", "run"))
