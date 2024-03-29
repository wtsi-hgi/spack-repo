# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdoutlier(RPackage):
	"""Distance & Density-Based Outlier Detection

	Outlier detection in multidimensional domains. Implementation of notable distance and density-based outlier algorithms. Allows users to identify local outliers by comparing observations to their nearest neighbors, reverse nearest neighbors, shared neighbors or natural neighbors. For distance-based approaches, see Knorr, M., & Ng, R. T. (1997) <doi:10.1145/782010.782021>, Angiulli, F., & Pizzuti, C. (2002) <doi:10.1007/3-540-45681-3_2>, Hautamaki, V., & Ismo, K. (2004) <doi:10.1109/ICPR.2004.1334558> and Zhang, K., Hutter, M. & Jin, H. (2009) <doi:10.1007/978-3-642-01307-2_84>. For density-based approaches, see Tang, J., Chen, Z., Fu, A. W. C., & Cheung, D. W. (2002) <doi:10.1007/3-540-47887-6_53>, Jin, W., Tung, A. K. H., Han, J., & Wang, W. (2006) <doi:10.1007/11731139_68>, Schubert, E., Zimek, A. & Kriegel, H-P. (2014) <doi:10.1137/1.9781611973440.63>, Latecki, L., Lazarevic, A. & Prokrajac, D. (2007) <doi:10.1007/978-3-540-73499-4_6>, Papadimitriou, S., Gibbons, P. B., & Faloutsos, C. (2003) <doi:10.1109/ICDE.2003.1260802>, Breunig, M. M., Kriegel, H.-P., Ng, R. T., & Sander, J. (2000) <doi:10.1145/342009.335388>, Kriegel, H.-P., Kröger, P., Schubert, E., & Zimek, A. (2009) <doi:10.1145/1645953.1646195>, Zhu, Q., Feng, Ji. & Huang, J. (2016) <doi:10.1016/j.patrec.2016.05.007>, Huang, J., Zhu, Q., Yang, L. & Feng, J. (2015) <doi:10.1016/j.knosys.2015.10.014>, Tang, B. & Haibo, He. (2017) <doi:10.1016/j.neucom.2017.02.039> and Gao, J., Hu, W., Zhang, X. & Wu, Ou. (2011) <doi:10.1007/978-3-642-20847-8_23>.
	"""
	
	homepage = "https://github.com/jhmadsen/DDoutlier"
	cran = "DDoutlier" 

	version("0.1.0", md5="a3683753caa03b0adbfafe33a25ca0a8")

	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
