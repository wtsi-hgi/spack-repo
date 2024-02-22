# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmdme(RPackage):
	"""Linear Model decomposition for Designed Multivariate Experiments

	linear ANOVA decomposition of Multivariate Designed Experiments implementation based on limma lmFit. Features: i)Flexible formula type interface, ii) Fast limma based implementation, iii) p-values for each estimated coefficient levels in each factor, iv) F values for factor effects and v) plotting functions for PCA and PLS.
	"""
	
	homepage = "http://www.bdmg.com.ar/?page_id=38"
	bioc = "lmdme" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/lmdme_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/lmdme/lmdme_1.44.0.tar.gz"]

	version("1.44.0", md5="9a1b98d738df482adb30496ac028b924")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-stemhypoxia", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
