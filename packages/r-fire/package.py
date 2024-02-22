# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFire(RPackage):
	"""Finder of Rare Entities (FiRE)

	The algorithm assigns rareness/ outlierness score to every sample in voluminous datasets.
    The algorithm makes multiple estimations of the proximity between a pair of samples, in low-dimensional spaces. To compute proximity, FiRE uses Sketching, a variant of locality sensitive hashing. For more details: Jindal, A., Gupta, P., Jayadeva and Sengupta, D., 2018. Discovery of rare cells from voluminous single cell expression data. Nature Communications, 9(1), p.4719. <doi:10.1038/s41467-018-07234-6>.
	"""
	
	homepage = "https://github.com/princethewinner/FiRE"
	cran = "FiRE" 

	version("1.0.1", md5="ce1956548a66bac9266f898985f38149")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
