# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabricerin(RPackage):
	"""Create Easily Canvas in 'shiny' and 'RMarkdown' Documents

	Allows the user to implement easily canvas elements within a 'shiny' app or an 'RMarkdown' document. 
    The user can create shapes, images and text elements within the canvas which can also be used as a drawing tool for taking notes.
    The package relies on the 'fabricjs' 'JavaScript' library. See <http://fabricjs.com/>.
	"""
	
	homepage = "https://github.com/feddelegrand7/fabricerin"
	cran = "fabricerin" 

	version("0.1.2", md5="d0a5d1c20ffb221cd075612669be5772")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
