# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtropical(RPackage):
	"""Data Analysis Tools over Space of Phylogenetic Trees Using
Tropical Geometry

	Process phylogenetic trees with tropical support vector machine and principal component analysis defined with tropical geometry. Details about tropical support vector machine are available in : Tang, X., Wang, H. & Yoshida, R. (2020) <arXiv:2003.00677>. Details about tropical principle component analysis are available in : Page, R., Yoshida, R. & Zhang L. (2020) <doi:10.1093/bioinformatics/btaa564> and Yoshida, R., Zhang, L. & Zhang, X. (2019) <doi:10.1007/s11538-018-0493-4>.
	"""
	
	homepage = "https://github.com/HoujieWang/Rtropical"
	cran = "Rtropical" 

	version("1.2.1", md5="0338edbbd92b87b28e2ed296e4385031")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
