# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgof(RPackage):
	"""Multiple Hypothesis Testing

	Seven different methods for multiple testing problems. The SGoF-type methods (see for example, Carvajal Rodríguez et al., 2009 <doi:10.1186/1471-2105-10-209>;  de Uña Álvarez, 2012 <doi:10.1515/1544-6115.1812>; Castro Conde et al., 2015 <doi:10.1177/0962280215597580>) and the BH and BY false discovery rate controlling procedures.
	"""
	
	cran = "sgof" 

	version("2.3.4", md5="5040fb4a766939343bd02fed1a9ab471")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-poibin", type=("build", "run"))
