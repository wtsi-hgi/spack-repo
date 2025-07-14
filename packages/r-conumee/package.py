# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConumee(RPackage):
	"""Enhanced copy-number variation analysis using Illumina DNA methylation arrays

	This package contains a set of processing and plotting methods for performing copy-number variation (CNV) analysis using Illumina 450k or EPIC methylation arrays.
	"""
	
	bioc = "conumee" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/conumee_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/conumee/conumee_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="e75a0aff3bcd1246d15841de749e211fbbe9be12d50e2012e8bb5e3e8a00c8f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b2-hg19", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
