# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicstate(RPackage):
	"""Build and access GenomicState objects for use with derfinder tools from sources like Gencode

	This package contains functions for building GenomicState objects from different annotation sources such as Gencode. It also provides access to these files at JHPCE.
	"""
	
	homepage = "https://github.com/LieberInstitute/GenomicState"
	bioc = "GenomicState" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/GenomicState_0.99.15.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/GenomicState/GenomicState_0.99.15.tar.gz"]

    version("0.99.16", tag="RELEASE_3_21")
	version("0.99.15", sha256="30d043091a1275290fa712865566824dd6cb4b78faac222963a265cf8d1dffe4")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-derfinder@1.21.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))

