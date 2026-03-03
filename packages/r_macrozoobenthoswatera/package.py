# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacrozoobenthoswatera(RPackage):
	"""Fresh Water Quality Analysis Based on Macrozoobenthos

	Includes functions  for calculating basic indices of macrozoobenthos for water quality and is designed to provide researchers and environmental professionals with a comprehensive tool for evaluating the ecological health of aquatic ecosystems.The package is based on the following references: Paisley, M. F., Trigg, D. J. and Walley, W. J. (2014)<doi:10.1002/rra.2686>. Arslan, N., Salur, A., Kalyoncu, H. et al.(2016)  <doi:10.1515/biolog-2016-0005>. Hilsenhoff W.L. (1987). Hilsenhoff. W.L. (1988)  Barbour, M.T., Gerritsen, J., Snyder, B.D., and Stribling, J.B. (1999).
	"""
	
	cran = "MacroZooBenthosWaterA" 

	version("0.1.0", md5="89c7f8311797a06e4b51de428d6054aa")

