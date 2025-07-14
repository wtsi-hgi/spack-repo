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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioCartaImage_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioCartaImage/BioCartaImage_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="69b3c5c40dd8d896714b644630bb8b579ec08c61f2114bfc7049c047b7fde076")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
