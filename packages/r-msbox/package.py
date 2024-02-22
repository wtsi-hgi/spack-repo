# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbox(RPackage):
	"""Mass Spectrometry Tools

	Common mass spectrometry tools described in John Roboz (2013) <doi:10.1201/b15436>. It allows checking element
 isotopes, calculating (isotope labelled) exact monoisitopic mass, m/z values and mass accuracy, and inspecting possible contaminant mass peaks,
 examining possible adducts in electrospray ionization (ESI) and matrix-assisted laser desorption ionization (MALDI)
 ion sources. 
	"""
	
	homepage = "https://github.com/YonghuiDong/MSbox"
	cran = "MSbox" 

	version("1.4.8", md5="ddaf26feaf79b1338da09f3f439a1117")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
