# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombinit(RPackage):
	"""A Combined Interaction Test for Unreplicated Two-Way Tables

	There are several non-functional-form-based interaction tests for testing interaction in unreplicated two-way layouts. However, no single test can detect all patterns of possible interaction and the tests are sensitive to a particular pattern of interaction. This package combines six non-functional-form-based interaction tests for testing additivity. These six tests were proposed by Boik (1993) <doi:10.1080/02664769300000004>, Piepho (1994), Kharrati-Kopaei and Sadooghi-Alvandi (2007) <doi:10.1080/03610920701386851>, Franck et al. (2013) <doi:10.1016/j.csda.2013.05.002>, Malik et al. (2016) <doi:10.1080/03610918.2013.870196> and Kharrati-Kopaei and Miller (2016) <doi:10.1080/00949655.2015.1057821>. The p-values of these six tests are combined by Bonferroni, Sidak, Jacobi polynomial expansion, and the Gaussian copula methods to provide researchers with a testing approach which leverages many existing methods to detect disparate forms of non-additivity. This package is based on the following published paper: Shenavari and Kharrati-Kopaei (2018) "A Method for Testing Additivity in Unreplicated Two-Way Layouts Based on Combining Multiple Interaction Tests". In addition, several sentences in help files or descriptions were copied from that paper.
	"""
	
	homepage = "https://github.com/haghbinh/combinIT"
	cran = "combinIT" 

	version("2.0.0", md5="48869ad871e18ed72e120f718caa42da")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
