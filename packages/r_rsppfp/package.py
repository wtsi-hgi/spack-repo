# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsppfp(RPackage):
	"""R's Shortest Path Problem with Forbidden Subpaths

	An implementation of functionalities to transform directed graphs that are bound to a set of
  known forbidden paths. There are several transformations, following the rules provided by Villeneuve 
  and Desaulniers (2005) <doi: 10.1016/j.ejor.2004.01.032>, and Hsu et al. (2009) <doi: 10.1007/978-3-642-03095-6_60>. 
  The resulting graph is generated in a data-frame format. See rsppfp website for more information, 
  documentation an examples.
	"""
	
	homepage = "https://github.com/melvidoni/rsppfp"
	cran = "rsppfp" 

	version("1.0.4", md5="15853382b45e3522ee3397c1d1fa8bcc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
