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

    version("1.84.0", tag="RELEASE_3_21")
	version("1.78.0", sha256="e47835a9ea6818f00d8c6c1335afeab52cba300384157772ba529c586a81a21b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
