# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRintimg(RPackage):
	"""View Images on Full Screen in 'RMarkdown' Documents and 'shiny'
Applications

	Allows the user to view an image in full screen when clicking on it in 'RMarkdown' documents and 'shiny' applications. 
  The package relies on the 'JavaScript' library 'intense-images'. See <https://tholman.com/intense-images/> for more information.
	"""
	
	homepage = "https://github.com/feddelegrand7/rintimg"
	cran = "rintimg" 

	version("0.1.0", md5="4a483ea19cb66d944a5542137edaa0e4")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
