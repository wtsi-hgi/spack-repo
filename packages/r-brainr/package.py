# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrainr(RPackage):
	"""Helper Functions to 'misc3d' and 'rgl' Packages for Brain
Imaging

	This includes functions for creating 3D and 4D images using 
    'WebGL', 'rgl', and 'JavaScript' commands.  
    This package relies on the X toolkit ('XTK',
    <https://github.com/xtk/X#readme>).
	"""
	
	cran = "brainR" 

	version("1.6.0", md5="b21261d19ffe8c3c396699d608eefdfb")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
