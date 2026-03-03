# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWskm(RPackage):
	"""Weighted k-Means Clustering

	Entropy weighted k-means (ewkm) by Liping Jing, Michael
        K. Ng and Joshua Zhexue Huang (2007)
        <doi:10.1109/TKDE.2007.1048> is a weighted subspace clustering
        algorithm that is well suited to very high dimensional data.
        Weights are calculated as the importance of a variable with
        regard to cluster membership.  The two-level variable
        weighting clustering algorithm tw-k-means (twkm) by Xiaojun
        Chen, Xiaofei Xu, Joshua Zhexue Huang and Yunming Ye (2013)
        <doi:10.1109/TKDE.2011.262> introduces two types of weights,
        the weights on individual variables and the weights on
        variable groups, and they are calculated during the clustering
        process.  The feature group weighted k-means (fgkm) by Xiaojun
        Chen, Yunminng Ye, Xiaofei Xu and Joshua Zhexue Huang (2012)
        <doi:10.1016/j.patcog.2011.06.004> extends this concept by
        grouping features and weighting the group in addition to
        weighting individual features.
	"""
	
	homepage = "https://github.com/SimonYansenZhao/wskm"
	cran = "wskm" 

	version("1.4.40", md5="d7bac26315b97fae190674c5fa317895")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
