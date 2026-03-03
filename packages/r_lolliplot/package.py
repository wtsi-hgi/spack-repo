# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLolliplot(RPackage):
	"""Plot Variants and Somatic Mutations

	Draw lolliplot using GRanges objects. this package was designed 
  only for drawing lolliplot. So, it's faster than 'trackViewer', but un-related 
  functions has been derived.
	"""
	
	cran = "lolliplot" 

	version("0.2.2", md5="ad936fe9400fe2cd671d1239ccbf0fad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-grimport", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
