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

	version("1.48.0", commit="b01670074d52c0cdbcc9a5154ba716e034161065")
	version("1.42.0", commit="4b13ebc5a8e5008124f86dd8cd379f1d683a77cf")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-noiseq", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
