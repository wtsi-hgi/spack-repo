# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqentangle(RPackage):
	"""Quantum Entanglement of Bipartite System

	It computes the Schmidt decomposition of bipartite quantum systems, discrete or continuous,
    and their respective entanglement metrics. See Artur Ekert, Peter L. Knight (1995) <doi:10.1119/1.17904> 
    for more details.
	"""
	
	homepage = "https://github.com/stephenhky/RQEntangle"
	cran = "RQEntangle" 

	version("0.1.3", md5="57009ae5d802b720b87516c2d2d6f5e5")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-itertools@0.1.3:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
