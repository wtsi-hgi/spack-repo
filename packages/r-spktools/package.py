# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpktools(RPackage):
	"""Methods for Spike-in Arrays

	The package contains functions that can be used to compare expression measures on different array platforms.
	"""
	
	homepage = "http://bioconductor.org"
	bioc = "spkTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spkTools_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spkTools/spkTools_1.58.0.tar.gz"]

    version("1.64.0", tag="RELEASE_3_21")
	version("1.58.0", sha256="a49043efbb289e10024f38c92c67228767b72345eb81c9f690479eb5428c82b2")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
