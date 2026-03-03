# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTml(RPackage):
	"""Tropical Geometry Tools for Machine Learning

	Suite of tropical geometric tools for use in machine learning applications. These methods may be summarized in the following references: Yoshida, et al. (2022) <arxiv:2209.15045>, Barnhill et al. (2023) <arxiv:2303.02539>, Barnhill and Yoshida (2023) <doi:10.3390/math11153433>, Aliatimis et al. (2023) <arXiv:2306.08796>, Yoshida et al. (2022) <arXiv:2206.04206>, and Yoshida et al. (2019) <doi:10.1007/s11538-018-0493-4>.
	"""
	
	homepage = "https://github.com/barnhilldave/TML"
	cran = "TML" 

	version("1.2.0", md5="75dc7a5cc48cc73bb6e859788a01ba7d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
