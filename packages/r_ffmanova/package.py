# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfmanova(RPackage):
	"""Fifty-Fifty MANOVA

	General linear modeling with multiple responses (MANCOVA). An overall p-value for each model term is calculated by the 50-50 MANOVA method by Langsrud (2002) <doi:10.1111/1467-9884.00320>, which handles collinear responses. Rotation testing, described by Langsrud (2005) <doi:10.1007/s11222-005-4789-5>, is used to compute adjusted single response p-values according to familywise error rates and false discovery rates (FDR). The approach to FDR is described in the appendix of Moen et al. (2005) <doi:10.1128/AEM.71.4.2086-2094.2005>. Unbalanced designs are handled by Type II sums of squares as argued in Langsrud (2003) <doi:10.1023/A:1023260610025>. Furthermore, the Type II philosophy is extended to continuous design variables as described in Langsrud et al. (2007) <doi:10.1080/02664760701594246>. This means that the method is invariant to scale changes and that common pitfalls are avoided.
	"""
	
	homepage = "https://github.com/olangsrud/ffmanova"
	cran = "ffmanova" 

	version("1.1.2", md5="8d45558c75e3812b190957d827a04c5f")

