# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaseq(RPackage):
	"""Meta-analysis of RNA-Seq count data in multiple studies

	The probabilities by one-sided NOISeq are combined by Fisher's method or Stouffer's method
	"""
	
	bioc = "metaSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metaSeq_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metaSeq/metaSeq_1.42.0.tar.gz"]

	version("1.42.0", sha256="16d0efef162c0ca1dab0448c6d58d52b8594740175cfc1c69a1e3439d0f374f7")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-noiseq", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
