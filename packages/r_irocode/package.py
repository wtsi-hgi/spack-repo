# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrocode(RPackage):
	"""Incomplete Row-Column Designs

	The Row-column designs are widely recommended for experimental situations when there are two well-identified factors that are cross-classified representing known sources of variability. These designs are expected to result a gain in accuracy of estimating treatment comparisons in an experiment as they eliminate the effects of the row and column factors. However, these designs are not readily available when the number of treatments is more than the levels of row and column blocking factors. This package named 'iRoCoDe' generates row-column designs with incomplete rows and columns, by amalgamating two incomplete block designs (D1 and D2). The selection of D1 and D2 (the input designs) can be done from the available incomplete block designs, viz., balanced incomplete block designs/ partially balanced incomplete block designs/ t-designs. (Mcsorley, J.P., Phillips, N.C., Wallis, W.D. and Yucas, J.L. (2005).<doi:10.1007/s10623-003-6149-9>).
	"""
	
	cran = "iRoCoDe" 

	version("1.0.1", md5="0b615aef88fe9cbab200ba56a0d55a0d")

