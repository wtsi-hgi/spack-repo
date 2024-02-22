# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmwra(RPackage):
	"""Multivariate Statistical Methods with R Applications

	Data sets in the book entitled "Multivariate Statistical Methods with R Applications", H.Bulut (2018). 
             The book was published in Turkish and the original name of this book will be "R Uygulamalari ile Cok Degiskenli Istatistiksel Yontemler".
	"""
	
	cran = "MSMwRA" 

	version("1.5", md5="ab800bf6a3c1699a71a0cc6d3861ad80")

