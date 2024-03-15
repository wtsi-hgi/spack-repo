# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS4arrays(RPackage):
	"""Foundation of array-like containers in Bioconductor

	The S4Arrays package defines the Array virtual class to be extended by other S4 classes that wish to implement a container with an array-like semantic. It also provides: (1) low-level functionality meant to help the developer of such container to implement basic operations like display, subsetting, or coercion of their array-like objects to an ordinary matrix or array, and (2) a framework that facilitates block processing of array-like objects (typically on-disk objects).
	"""
	
	homepage = "https://bioconductor.org/packages/S4Arrays"
	bioc = "S4Arrays" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/S4Arrays_1.2.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/S4Arrays/S4Arrays_1.2.1.tar.gz"]

	version("1.2.1", md5="56e78d721cbf2dc16d12123dca444272")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-biocgenerics@0.45.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
