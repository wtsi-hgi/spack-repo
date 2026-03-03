# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGggrid(RPackage):
	"""Draw with 'grid' in 'ggplot2'

	An extension of 'ggplot2' that makes it easy to add
             raw 'grid' output, such as customised annotations, to a 
             'ggplot2' plot.  
	"""
	
	homepage = "https://github.com/pmur002/gggrid"
	cran = "gggrid" 

	version("0.2-0", md5="62c71fbb5eb60537a1f6e27420b908b9")

	depends_on("r-ggplot2", type=("build", "run"))
