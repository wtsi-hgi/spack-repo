# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvert(RPackage):
	"""Convert Microarray Data Objects

	Define coerce methods for microarray data objects.
	"""
	
	homepage = "http://bioinf.wehi.edu.au/limma/convert.html"
	bioc = "convert" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/convert_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/convert/convert_1.78.0.tar.gz"]

	version("1.78.0", md5="828a21b5a554d63faeb6cc2af0784394")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase@1.15.33:", type=("build", "run"))
	depends_on("r-limma@1.7:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
