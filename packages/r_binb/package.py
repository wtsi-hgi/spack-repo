# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinb(RPackage):
	"""'binb' is not 'Beamer'

	A collection of 'LaTeX' styles using 'Beamer' customization for
 pdf-based presentation slides in 'RMarkdown'. At present it contains
 'RMarkdown' adaptations of the LaTeX themes 'Metropolis' (formerly 'mtheme')
 theme by Matthias Vogelgesang and others (now included in 'TeXLive'), the
 'IQSS' by Ista Zahn (which is included here), and the 'Monash' theme by
 Rob J Hyndman. Additional (free) fonts may be needed: 'Metropolis' prefers
 'Fira', and 'IQSS' requires 'Libertinus'.
	"""
	
	homepage = "https://github.com/eddelbuettel/binb"
	cran = "binb" 

	version("0.0.6", md5="bd41f8f5f5dc1a4fea6c1994a836f6a1")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
