# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPliman(RPackage):
	"""Tools for Plant Image Analysis

	Tools for single or batch image manipulation and analysis as
    described by Olivoto (2022) <doi:10.1111/2041-210X.13803> that can be
    used to quantify plant leaf area, assess disease severity, count
    objects, obtain shape measures, object landmarks, and compute
    Elliptical Fourier Analysis of the object outline, as described by
    Claude (2008) <doi:10.1007/978-0-387-77789-4>. Additionally, the
    package includes tools for analyzing grids, which enables high
    throughput field phenotyping using RGB imagery captured by unmanned
    aerial vehicles.
	"""
	
	homepage = "https://github.com/TiagoOlivoto/pliman"
	cran = "pliman" 

	version("2.1.0", md5="127b40df7d97040d5b631e1a6ea1e954")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
