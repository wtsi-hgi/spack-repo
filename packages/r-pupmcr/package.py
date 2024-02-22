# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPupmcr(RPackage):
	"""Image-Based Identification of Color Based on Rayner (1970)
Terminology and Known Fungal Pigments

	Image-based color matching using the "Mycological Colour Chart" by Rayner (1970, ISBN:9780851980263) and its associated fungal pigments. This package will assist mycologists in identifying color during morphological analysis.
	"""
	
	cran = "PUPMCR" 

	version("0.2.0", md5="7ad8bf71c51c88a6eff49efd73c4c161")

	depends_on("r-colordistance", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
