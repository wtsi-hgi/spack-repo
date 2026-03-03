# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdthap(RPackage):
	"""TDT Tests for Extended Haplotypes

	Functions and examples are provided for Transmission/disequilibrium tests
             for extended marker haplotypes, as in
             Clayton, D. and Jones, H. (1999) "Transmission/disequilibrium tests
             for extended marker haplotypes". Amer. J. Hum. Genet., 65:1161-1169,
             <doi:10.1086/302566>.
	"""
	
	homepage = "https://github.com/jinghuazhao/R"
	cran = "tdthap" 

	version("1.3", md5="ff63a515a996e951f760a14363f468eb")

	depends_on("r@1.5:", type=("build", "run"))
