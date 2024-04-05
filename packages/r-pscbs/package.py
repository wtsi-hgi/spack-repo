# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPscbs(RPackage):
	"""Analysis of Parent-Specific DNA Copy Numbers.

	Segmentation of allele-specific DNA copy number data and detection of
	regions with abnormal copy number within each parental chromosome. Both
	tumor-normal paired and tumor-only analyses are supported."""

	cran = "PSCBS"
	version("0.67.0", md5="df9193fb19fb791450f243cea604a29b")
	version("0.66.0", sha256="58805636e55e0fd3f57bd4a0e296a8bb3d57a7bdd0fdd5868a73ddc83d173a93")
	version("0.65.0", sha256="3365065d5375c599eb024bfff12c5f6b10a6b1a4fe4ba6f200f7e83618dd399a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r-methodss3@1.8.2:", type=("build", "run"))
	depends_on("r-r-oo@1.25:", type=("build", "run"))
	depends_on("r-r-utils@2.12:", type=("build", "run"))
	depends_on("r-r-cache@0.16:", type=("build", "run"))
	depends_on("r-matrixstats@0.62:", type=("build", "run"))
	depends_on("r-aroma-light@2.4:", type=("build", "run"))
	depends_on("r-dnacopy@1.42:", type=("build", "run"))
	depends_on("r-listenv@0.8:", type=("build", "run"))
	depends_on("r-future@1.28:", type=("build", "run"))
