# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl(RPackage):
	"""Tools for Analyzing QTL Experiments.

	Analysis of experimental crosses to identify genes (called quantitative
	trait loci, QTLs) contributing to variation in quantitative traits. Broman
	et al. (2003) <doi:10.1093/bioinformatics/btg112>."""

	cran = "qtl"

	version("1.66", md5="6b196598f827825cf7c9063fb740b61e")

	depends_on("r@2.14:", type=("build", "run"))
