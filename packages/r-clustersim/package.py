# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustersim(RPackage):
	"""Searching for Optimal Clustering Procedure for a Data Set

	Distance measures (GDM1, GDM2,	Sokal-Michener, Bray-Curtis, for symbolic interval-valued data), cluster quality indices (Calinski-Harabasz, Baker-Hubert, Hubert-Levine, Silhouette, Krzanowski-Lai, Hartigan, Gap,	Davies-Bouldin),	data normalization formulas (metric data, interval-valued symbolic data), data generation (typical and non-typical data), HINoV method,	replication analysis, linear ordering methods, spectral clustering, agreement indices between two partitions, plot functions (for categorical and symbolic interval-valued data). 
 (MILLIGAN, G.W., COOPER, M.C. (1985) <doi:10.1007/BF02294245>, 
 HUBERT, L., ARABIE, P. (1985) <doi:10.1007%2FBF01908075>, 
 RAND, W.M. (1971) <doi:10.1080/01621459.1971.10482356>, 
 JAJUGA, K., WALESIAK, M. (2000) <doi:10.1007/978-3-642-57280-7_11>, 
 MILLIGAN, G.W., COOPER, M.C. (1988) <doi:10.1007/BF01897163>, 
 JAJUGA, K., WALESIAK, M., BAK, A. (2003) <doi:10.1007/978-3-642-55721-7_12>, 
 DAVIES, D.L., BOULDIN, D.W. (1979) <doi:10.1109/TPAMI.1979.4766909>, 
 CALINSKI, T., HARABASZ, J. (1974) <doi:10.1080/03610927408827101>,
 HUBERT, L. (1974) <doi:10.1080/01621459.1974.10480191>, 
 TIBSHIRANI, R., WALTHER, G., HASTIE, T. (2001) <doi:10.1111/1467-9868.00293>, 
 BRECKENRIDGE, J.N. (2000) <doi:10.1207/S15327906MBR3502_5>, 
 WALESIAK, M., DUDEK, A. (2008) <doi:10.1007/978-3-540-78246-9_11>).
	"""
	
	homepage = "http://keii.ue.wroc.pl/clusterSim/"
	cran = "clusterSim" 

	version("0.51-3", md5="e3b1a52d89ac233a1750722a52257d33")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
