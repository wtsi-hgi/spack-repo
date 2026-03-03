# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTipdatingbeast(RPackage):
	"""Using Tip Dates with Phylogenetic Trees in BEAST

	Assists performing tip-dating of phylogenetic trees with BEAST 
    BEAST is a popular software for phylogenetic analysis.
    The package assists the implementation of various phylogenetic tip-
	dating tests using BEAST. It contains two main functions.
	The first one allows preparing date randomization analyses, 
	which assess the temporal signal of a data set. 
	The second function allows performing leave-one-out analyses,
	which test for the consistency between independent calibration sequences
	and allow pinpointing those leading to potential bias.
	The included tutorial provides detailed step-by-step instructions.
	An expanded description of the package can be found in article:
	Rieux, A. and Khatchikian, C.E. (2017), 
	TIPDATINGBEAST: an R package to assist the implementation of phylogenetic
	tip-dating tests using BEAST. Molecular Ecology Resources, 17: 608-613.
	<onlinelibrary.wiley.com/doi/full/10.1111/1755-0998.12603>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "TipDatingBeast" 

	version("1.1-0", md5="9eccb69be14a8dbea4aa739f5f69d840")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
