# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrollrevealr(RPackage):
	"""Animate 'shiny' Elements when They Scroll into View using the
'scrollrevealjs' Library

	Allows the user to animate 'shiny' elements when scrolling to view them.
    The animations are activated using the 'scrollrevealjs' library. See <https://scrollrevealjs.org/> for more information.
	"""
	
	homepage = "https://github.com/feddelegrand7/scrollrevealR"
	cran = "scrollrevealR" 

	version("0.2.0", md5="1c4c6722b917c8aff27dbec444fc0bd2")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
