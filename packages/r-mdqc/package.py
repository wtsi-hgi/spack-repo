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

	version("1.70.0", commit="0ddfba7a98071dbfc1e3fd1f542c3c2380838d93")
	version("1.64.0", commit="422e9ec92527d71903cd7cbc72944113b51812cc")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
