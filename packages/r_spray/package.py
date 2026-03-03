# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpray(RPackage):
	"""Sparse Arrays and Multivariate Polynomials

	Sparse arrays interpreted as multivariate polynomials.
    Uses 'disordR' discipline (Hankin, 2022,
    <doi:10.48550/ARXIV.2210.03856>).  To cite the package in
    publications please use Hankin (2022) <doi:10.48550/ARXIV.2210.10848>.
	"""
	
	homepage = "https://github.com/RobinHankin/spray"
	cran = "spray" 

	version("1.0-25", md5="ebc345de13fe2220e98da589140b1b33")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.9.6:", type=("build", "run"))
