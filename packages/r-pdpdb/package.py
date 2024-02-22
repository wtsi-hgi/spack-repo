# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdpdb(RPackage):
	"""Pattern Discovery in PDB Structures of Metalloproteins

	Looks for amino acid and/or nucleotide patterns and/or small
    ligands coordinated to a given prosthetic centre. Files have to be in the local
    file system and contain proper extension.
	"""
	
	cran = "PdPDB" 

	version("2.0.1", md5="957650e3e691f74f9922502e525c9df7")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
