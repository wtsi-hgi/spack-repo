# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResemble(RPackage):
	"""Memory-Based Learning in Spectral Chemometrics

	
    Functions for dissimilarity analysis and memory-based learning 
    (MBL, a.k.a local modeling) in complex spectral data sets. 
    Most of these functions are based on the methods presented in 
    Ramirez-Lopez et al. (2013) <doi:10.1016/j.geoderma.2012.12.014>.
	"""
	
	homepage = "http://l-ramirez-lopez.github.io/resemble/"
	cran = "resemble" 

	version("2.2.3", md5="3aa9742c8fb807c26dc4933970271387")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mathjaxr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
