# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLineup2(RPackage):
	"""Lining Up Two Sets of Measurements

	Tools for detecting and correcting sample mix-ups between two sets
    of measurements, such as between gene expression data on two
    tissues. This is a revised version of the 'lineup' package, to be
    more general and not tied to the 'qtl' package.
	"""
	
	homepage = "https://github.com/kbroman/lineup2"
	cran = "lineup2" 

	version("0.6", md5="21cdc58a841de0e7d7d35c9004817e2a", url="https://cran.r-project.org/src/contrib/lineup2_0.6.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
