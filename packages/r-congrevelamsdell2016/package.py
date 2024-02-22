# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCongrevelamsdell2016(RPackage):
	"""Distance Metrics for Trees Generated by Congreve and Lamsdell

	Includes the 100 datasets simulated by Congreve and Lamsdell (2016)
  <doi:10.1111/pala.12236>, and analyses of the partition and quartet distance of
  reconstructed trees from the generative tree, as analysed by Smith (2019)
  <doi:10.1098/rsbl.2018.0632>.
	"""
	
	homepage = "https://github.com/ms609/CongreveLamsdell2016"
	cran = "CongreveLamsdell2016" 

	version("1.0.2", md5="b35997e74d981ae679c37082757cc065", url="https://cran.r-project.org/src/contrib/CongreveLamsdell2016_1.0.2.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ternary", type=("build", "run"))
