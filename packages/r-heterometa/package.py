# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeterometa(RPackage):
	"""Convert Various Meta-Analysis Heterogeneity Measures

	Published meta-analyses routinely present one of the
   measures of heterogeneity introduced in Higgins and Thompson
   (2002) <doi:10.1002/sim.1186>. For critiquing articles
   it is often better to convert to another measure. Some
   conversions are provided here and confidence intervals are also
   available.
	"""
	
	cran = "heterometa" 

	version("0.2", md5="fdb55cec587cb7e1e50cbdaf418cd091")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-mathjaxr@0.8.3:", type=("build", "run"))
