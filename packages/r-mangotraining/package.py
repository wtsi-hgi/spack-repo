# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMangotraining(RPackage):
	"""Mango Solutions Training Datasets

	Datasets to be used primarily in conjunction with Mango Solutions
    training materials but also for the book 'SAMS Teach Yourself R in 24 Hours' (ISBN: 978-0-672-33848-9).
    Version 1.0-7 is largely for use with the book; however, version 1.1 has a much greater focus on use with
    training materials, whilst retaining compatibility with the book.
	"""
	
	homepage = "https://www.mango-solutions.com/"
	cran = "mangoTraining" 

	version("1.1.1", md5="6d4d101cbd8f85377622825ca1360eda")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
