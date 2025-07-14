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

	version("1.50.0", commit="b7267a11f8b4abf78c3edb0369667ba1edaafa25")
	version("1.44.0", commit="714faa2f2276e1660c763de2065f8d11cc6921fb")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-stemhypoxia", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
