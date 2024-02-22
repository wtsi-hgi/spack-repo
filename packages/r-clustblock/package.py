# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustblock(RPackage):
	"""Clustering of Datasets

	Hierarchical and partitioning algorithms of blocks of variables. The partitioning algorithm includes an option called noise cluster to set aside atypical blocks of variables. The CLUSTATIS method (for quantitative blocks) (Llobell, Cariou, Vigneau, Labenne & Qannari (2020) <doi:10.1016/j.foodqual.2018.05.013>, Llobell, Vigneau & Qannari (2019) <doi:10.1016/j.foodqual.2019.02.017>)  and the CLUSCATA method (for Check-All-That-Apply data) (Llobell, Cariou, Vigneau, Labenne & Qannari (2019) <doi:10.1016/j.foodqual.2018.09.006>, Llobell, Giacalone, Labenne & Qannari (2019) <doi:10.1016/j.foodqual.2019.05.017>) are the core of this package. The CATATIS methods allows to compute some indices and tests to control the quality of CATA data. Multivariate analysis and clustering of subjects for quantitative multiblock data, CATA, RATA, Free Sorting and JAR experiments are available.
	"""
	
	cran = "ClustBlock" 

	version("3.2.0", md5="0c9b3dd34b30ba965f5a76c1bc348371")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
