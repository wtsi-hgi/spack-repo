# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyper2(RPackage):
	"""The Hyperdirichlet Distribution, Mark 2

	A suite of routines for the hyperdirichlet distribution;
   supersedes the 'hyperdirichlet' package.  Uses 'disordR' discipline.
	"""
	
	homepage = "https://github.com/RobinHankin/hyper2"
	cran = "hyper2" 

	version("3.0-0", md5="290d5c0ae6808f55e267b9c75292c075", url="https://cran.r-project.org/src/contrib/hyper2_3.0-0.tar.gz")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.0.9:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-calibrator", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
