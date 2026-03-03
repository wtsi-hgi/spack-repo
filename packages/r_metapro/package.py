# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetapro(RPackage):
	"""Robust P-Value Combination Methods

	The meta-analysis is performed to increase the statistical power by integrating the results from several experiments. The p-values are often combined in meta-analysis when the effect sizes are not available. The 'metapro' R package provides not only traditional methods (Becker BJ (1994, ISBN:0-87154-226-9), Mosteller, F. & Bush, R.R. (1954, ISBN:0201048523) and Lancaster HO (1949, ISSN:00063444)), but also new method named weighted Fisher’s method we developed. While the (weighted) Z-method is suitable for finding features effective in most experiments, (weighted) Fisher’s method is useful for detecting partially associated features. Thus, the users can choose the function based on their purpose. Yoon et al. (2021) "Powerful p-value combination methods to detect incomplete association" <doi:10.1038/s41598-021-86465-y>.
	"""
	
	cran = "metapro" 

	version("1.5.11", md5="87b01e28e70312dfc871621d5649c20c")

	depends_on("r-metap", type=("build", "run"))
