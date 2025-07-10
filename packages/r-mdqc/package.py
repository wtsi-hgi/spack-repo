# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdqc(RPackage):
	"""Mahalanobis Distance Quality Control for microarrays

	MDQC is a multivariate quality assessment method for microarrays based on quality control (QC) reports. The Mahalanobis distance of an array's quality attributes is used to measure the similarity of the quality of that array against the quality of the other arrays. Then, arrays with unusually high distances can be flagged as potentially low-quality.
	"""
	
	bioc = "mdqc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mdqc_1.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mdqc/mdqc_1.64.0.tar.gz"]

	version("1.64.0", sha256="8ede5bc1eae8540c551d4c68658e3dac603f027c3b6bcf9318490bd7707ad160")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
