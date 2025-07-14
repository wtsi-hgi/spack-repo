# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocartaimage(RPackage):
	"""BioCarta Pathway Images

	The core functionality of the package is to provide coordinates of genes on the BioCarta pathway images and to provide methods to add self-defined graphics to the genes of interest.
	"""
	
	homepage = "https://github.com/jokergoo/BioCartaImage"
	bioc = "BioCartaImage"

	version("1.6.0", commit="ab2381c65619f078ca82a21bb22b446757816d62")
	version("1.0.0", commit="1de111256540c98619bc6d10c9d680f21e58ec0a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
