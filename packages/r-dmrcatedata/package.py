# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrcatedata(RPackage):
	"""Data Package for DMRcate

	This package contains 9 data objects supporting functionality and examples of the Bioconductor package DMRcate.
	"""
	
	bioc = "DMRcatedata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DMRcatedata_2.20.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DMRcatedata/DMRcatedata_2.20.3.tar.gz"]

    version("2.26.0", tag="RELEASE_3_21")
	version("2.20.3", sha256="0ae00b8a0127f920c51ea964034bd05ebe0d543e478c31e01ec968606438133a")
	version("2.20.2", md5="0cd6e9693ca761425b661cd4a512d797")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b4-hg19", type=("build", "run"))

