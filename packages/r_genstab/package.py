# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenstab(RPackage):
	"""Resampling Based Yield Stability Analyses

	Several yield stability analyses are mentioned in this package: variation and regression based yield stability analyses. Resampling techniques are integrated with these stability analyses. The function stab.mean() provides the genotypic means and ranks including their corresponding confidence intervals. The function stab.var() provides the genotypic variances over environments including their corresponding confidence intervals. The function stab.fw() is an extended method from the Finlay-Wilkinson method (1963). This method can include several other factors that might impact yield stability. Resampling technique is integrated into this method. A few missing data points or unbalanced data are allowed too. The function stab.fw.check() is an extended method from the Finlay-Wilkinson method (1963). The yield stability is evaluated via common check line(s). Resampling technique is integrated.
	"""
	
	cran = "genstab" 

	version("1.0.0", md5="0bbae09c82303e64c96cf563de9aee22")

	depends_on("r@4:", type=("build", "run"))
