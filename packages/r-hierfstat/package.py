# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierfstat(RPackage):
	"""Estimation and Tests of Hierarchical F-Statistics

	Estimates hierarchical F-statistics from haploid or
    diploid genetic data with any numbers of levels in the hierarchy, following the
    algorithm of Yang (Evolution(1998), 52:950).
    Tests via randomisations the significance
    of each F and variance components, using the likelihood-ratio statistics G
    (Goudet et al. (1996) <https://academic.oup.com/genetics/article/144/4/1933/6017091>).
    Estimates genetic diversity statistics
    for haploid and diploid genetic datasets in various formats, including inbreeding and
    coancestry coefficients, and population specific F-statistics following
    Weir and Goudet (2017) <https://academic.oup.com/genetics/article/206/4/2085/6072590>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "hierfstat" 

	version("0.5-11", md5="9bc78ee3f9bbe0fe2ab9e44c5bff40cf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
