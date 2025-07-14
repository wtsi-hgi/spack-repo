# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnanorm(RPackage):
	"""A normalization method for Copy Number Aberration in cancer samples

	Performs ratio, GC content correction and normalization of data obtained using low coverage (one read every 100-10,000 bp) high troughput sequencing. It performs a "discrete" normalization looking for the ploidy of the genome. It will also provide tumour content if at least two ploidy states can be found.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "CNAnorm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNAnorm_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNAnorm/CNAnorm_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="050233377f5128c1713c2fc2be812069e1a7e593afac3a95c01b18a3a42fb905")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
