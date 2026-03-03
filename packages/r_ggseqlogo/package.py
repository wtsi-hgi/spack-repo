# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgseqlogo(RPackage):
	"""A 'ggplot2' Extension for Drawing Publication-Ready Sequence
Logos

	The extensive range of functions provided by this package makes it possible to draw highly versatile sequence logos. Features include, but not limited to, modifying colour schemes and fonts used to draw the logo, generating multiple logo plots, and aiding the visualisation with annotations. Sequence logos can easily be combined with other plots 'ggplot2' plots.
	"""
	
	homepage = "https://github.com/omarwagih/ggseqlogo"
	cran = "ggseqlogo" 

	version("0.2", md5="fc56efe0d4c088af705a5db076bc432d")

	depends_on("r-ggplot2", type=("build", "run"))
