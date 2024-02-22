# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTurbonorm(RPackage):
	"""A fast scatterplot smoother suitable for microarray normalization

	A fast scatterplot smoother based on B-splines with second-order difference penalty. Functions for microarray normalization of single-colour data i.e. Affymetrix/Illumina and two-colour data supplied as marray MarrayRaw-objects or limma RGList-objects are available.
	"""
	
	homepage = "http://www.humgen.nl/MicroarrayAnalysisGroup.html"
	bioc = "TurboNorm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TurboNorm_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TurboNorm/TurboNorm_1.50.0.tar.gz"]

	version("1.50.0", md5="6df6da83bc36e4ce202d91888feaafa7")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-convert", type=("build", "run"))
	depends_on("r-limma@1.7:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
