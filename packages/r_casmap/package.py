# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasmap(RPackage):
	"""Detection of Statistically Significant Combinations of SNPs in
Association Mapping

	A significant pattern mining-based toolbox for region-based genome-wide association studies and higher-order epistasis analyses, implementing the methods described in Llinares-López et al. (2017) <doi:10.1093/bioinformatics/btx071>.
	"""
	
	cran = "CASMAP" 

	version("0.6.1", md5="3386470ebe6725314aac2b5afe14035c")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
