# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSht(RPackage):
	"""Statistical Hypothesis Testing Toolbox

	We provide a collection of statistical hypothesis testing procedures ranging from classical to modern methods for non-trivial settings such as high-dimensional scenario. For the general treatment of statistical hypothesis testing, see the book by Lehmann and Romano (2005) <doi:10.1007/0-387-27605-X>.
	"""
	
	homepage = "https://www.kisungyou.com/SHT/"
	cran = "SHT" 

	version("0.1.8", md5="f180982ce6873c3d81e9fc5220fe272c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-flare", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
