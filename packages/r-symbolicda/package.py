# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymbolicda(RPackage):
	"""Analysis of Symbolic Data

	Symbolic data analysis methods: importing/exporting data from ASSO XML Files, distance calculation for symbolic data (Ichino-Yaguchi, de Carvalho measure), zoom star plot, 3d interval plot, multidimensional scaling for symbolic interval data, dynamic clustering based on distance matrix, HINoV method for symbolic data, Ichino's feature selection method, principal component analysis for symbolic interval data, decision trees for symbolic data based on optimal split with bagging, boosting and random forest approach (+visualization), kernel discriminant analysis for symbolic data, Kohonen's self-organizing maps for symbolic data, replication and profiling, artificial symbolic data generation.
 (Milligan, G.W., Cooper, M.C. (1985) <doi:10.1007/BF02294245>,
 Breiman, L. (1996), <doi:10.1007/BF00058655>,
 Hubert, L., Arabie, P. (1985), <doi:10.1007%2FBF01908075>,
 Ichino, M., & Yaguchi, H. (1994), <doi:10.1109/21.286391>,
 Rand, W.M. (1971) <doi:10.1080/01621459.1971.10482356>,
 Calinski, T., Harabasz, J. (1974) <doi:10.1080/03610927408827101>,
 Breckenridge, J.N. (2000) <doi:10.1207/S15327906MBR3502_5>,
 Groenen, P.J.F, Winsberg, S., Rodriguez, O., Diday, E. (2006) <doi:10.1016/j.csda.2006.04.003>,
 Walesiak, M., Dudek, A. (2008) <doi:10.1007/978-3-540-78246-9_11>,
 Dudek, A. (2007), <doi:10.1007/978-3-540-70981-7_4>).
	"""
	
	homepage = "http://keii.ue.wroc.pl/symbolicDA/"
	cran = "symbolicDA" 

	version("0.7-1", md5="3102126c5f866263b100b1a8ad584485")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rsda", type=("build", "run"))
