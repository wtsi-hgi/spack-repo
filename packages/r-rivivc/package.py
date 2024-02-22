# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRivivc(RPackage):
	"""In Vitro in Vivo Correlation Linear Level "A"

	It is devoted to the IVIVC linear level A with numerical deconvolution method. The latter is working for inequal and incompatible timepoints between impulse and response curves. A numerical convolution method is also available. Application domains include pharamaceutical industry QA/QC and R&D together with academic research.
	"""
	
	cran = "Rivivc" 

	version("0.9.1", md5="18a0327de5611ccbe11dc1691b581699")

	depends_on("r-signal", type=("build", "run"))
