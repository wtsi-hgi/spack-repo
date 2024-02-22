# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwascat(RPackage):
	"""representing and modeling data in the EMBL-EBI GWAS catalog

	Represent and model data in the EMBL-EBI GWAS catalog.
	"""
	
	bioc = "gwascat" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gwascat_2.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gwascat/gwascat_2.34.0.tar.gz"]

	version("2.34.0", md5="a7cbd1d5ac4b3d4fbb8d1fbd77269e44")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.29.6:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
