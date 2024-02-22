# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmac(RPackage):
	"""Data for Mathematical Modeling and Applied Calculus

	Contains the data sets for the textbook "Mathematical Modeling and Applied Calculus" by Joel Kilty and Alex M. McAllister. The book will be published by Oxford University Press in 2018 with ISBN-13: 978-019882472. 
	"""
	
	cran = "MMAC" 

	version("0.1.2", md5="d47622ce9a0aa516b3606305bc386a7c")

	depends_on("r@2.10:", type=("build", "run"))
