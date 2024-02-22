# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPirf(RPackage):
	"""Prediction Intervals for Random Forests

	Implements multiple state-of-the-art prediction interval methodologies for random forests. 
	These include: quantile regression intervals, out-of-bag intervals, bag-of-observations intervals, 
	one-step boosted random forest intervals, bias-corrected intervals, high-density intervals, and 
	split-conformal intervals. The implementations include a combination of novel adjustments to the 
	original random forest methodology and novel prediction interval methodologies. All of these 
	methodologies can be utilized using solely this package, rather than a collection of separate 
	packages. Currently, only regression trees are supported. Also capable of handling high dimensional data. 
	Roy, Marie-Helene and Larocque, Denis (2019) <doi:10.1177/0962280219829885>.
	Ghosal, Indrayudh and Hooker, Giles (2018) <arXiv:1803.08000>.
	Zhu, Lin and Lu, Jiaxin and Chen, Yihong (2019) <arXiv:1905.10101>.
	Zhang, Haozhe and Zimmerman, Joshua and Nettleton, Dan and Nordman, Daniel J. (2019) <doi:10.1080/00031305.2019.1585288>.
	Meinshausen, Nicolai (2006) <http://www.jmlr.org/papers/volume7/meinshausen06a/meinshausen06a.pdf>.
	Romano, Yaniv and Patterson, Evan and Candes, Emmanuel (2019) <arXiv:1905.03222>.
	Tung, Nguyen Thanh and Huang, Joshua Zhexue and Nguyen, Thuy Thi and Khan, Imran (2014) <doi:10.13140/2.1.2500.8002>.
	"""
	
	homepage = "http://github.com/chancejohnstone/piRF"
	cran = "piRF" 

	version("0.1.0", md5="800f9981871949c9c2dec12df0356184")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
