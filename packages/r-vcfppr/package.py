# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcfppr(RPackage):
	"""Rapid Manipulation of the Variant Call Format (VCF)

	The 'vcfpp.h' (<https://github.com/Zilong-Li/vcfpp>) provides an easy-to-use 'C++' 'API' of 'htslib', offering full functionality for manipulating Variant Call Format (VCF) files. The 'vcfppR' package serves as the R bindings of the 'vcfpp.h' library, enabling rapid processing of both compressed and uncompressed VCF/BCF files. Explore a range of powerful features for efficient VCF data manipulation.
	"""
	
	homepage = "https://github.com/Zilong-Li/vcfppR"
	cran = "vcfppR" 

	version("0.3.8", md5="9e2ffe5230dbd0982223e238afb927f0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("openssl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
