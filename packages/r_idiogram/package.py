# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdiogram(RPackage):
	"""idiogram

	A package for plotting genomic data by chromosomal location
	"""
	
	bioc = "idiogram" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/idiogram_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/idiogram/idiogram_1.78.0.tar.gz"]

	version("1.78.0", md5="2ee94ac9719c77f8a2f6b691662a7909")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
