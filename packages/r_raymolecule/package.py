# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaymolecule(RPackage):
	"""Parse and Render Molecular Structures in 3D

	Downloads and parses 'SDF' (Structural Description Format) and 'PDB' (Protein Database) files for 3D rendering.
	"""
	
	homepage = "http://www.raymolecule.com/"
	cran = "raymolecule" 

	version("0.5.3", md5="a8add651bfa33e529a281728b3e25a36")

	depends_on("r-rayrender@0.31.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-periodictable", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rayvertex@0.10.4:", type=("build", "run"))
