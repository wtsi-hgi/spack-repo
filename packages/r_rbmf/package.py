# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbmf(RPackage):
	"""Boolean Matrix Factorization

	Provides four boolean matrix factorization (BMF) methods.
             BMF has many applications like data mining and categorical data 
             analysis. BMF is also known as boolean matrix decomposition (BMD) 
             and was found to be an NP-hard (non-deterministic polynomial-time)
             problem. Currently implemented methods are 
             'Asso' Miettinen, Pauli and others (2008) 
                    <doi:10.1109/TKDE.2008.53>,
             'GreConD' R. Belohlavek, V. Vychodil (2010) 
                      <doi:10.1016/j.jcss.2009.05.002> ,
             'GreConDPlus' R. Belohlavek, V. Vychodil (2010) 
                      <doi:10.1016/j.jcss.2009.05.002> ,
             'topFiberM' A. Desouki, M. Roeder, A. Ngonga (2019) 
                       <arXiv:1903.10326>.
	"""
	
	cran = "rBMF" 

	version("1.1", md5="c2e9839d012e932ce4e571d5da8dae2b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
