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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BioCartaImage_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BioCartaImage/BioCartaImage_1.0.0.tar.gz"]

	version("1.0.0", md5="8190c93a49f3d53085b3e6e44d482ffa")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
