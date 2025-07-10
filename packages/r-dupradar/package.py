# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDupradar(RPackage):
	"""Assessment of duplication rates in RNA-Seq datasets

	Duplication rate quality control for RNA-Seq datasets.
	"""
	
	homepage = "https://www.bioconductor.org/packages/dupRadar"
	bioc = "dupRadar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/dupRadar_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/dupRadar/dupRadar_1.32.0.tar.gz"]

	version("1.32.0", sha256="40fc1818e109f4649a1f4c97c6c377355b5f4b5a1c2126ef16ea6b7789f3f018")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rsubread@1.14.1:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
