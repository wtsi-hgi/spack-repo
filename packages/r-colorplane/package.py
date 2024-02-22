# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorplane(RPackage):
	"""Basic S4 Classes and Methods for Mapping Between Numeric Values
and Colors

	A simple set of classes and methods for mapping between scalar intensity values and colors. There is also support for layering maps on top of one another using alpha composition. 
	"""
	
	cran = "colorplane" 

	version("0.5.0", md5="44a087de541f147f7880bf4b281e901c")

	depends_on("r-assertthat", type=("build", "run"))
