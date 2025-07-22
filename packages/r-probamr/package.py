# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbamr(RPackage):
	"""Generating SAM file for PSMs in shotgun proteomics data

	Mapping PSMs back to genome. The package builds SAM file from shotgun proteomics data The package also provides function to prepare annotation from GTF file.
	"""
	
	bioc = "proBAMr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/proBAMr_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/proBAMr/proBAMr_1.36.0.tar.gz"]

	version("1.36.0", sha256="3984b967cc0b8e5a853b7a2029fc6a996ac7fb55edae5569f4d33b8bc866c04a")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
