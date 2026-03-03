# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAscenttraining(RPackage):
	"""Ascent Training Datasets

	Datasets to be used primarily in conjunction with Ascent
    training materials but also for the book 'SAMS Teach Yourself R in 24 Hours' (ISBN: 978-0-672-33848-9).
    Version 1.0-7 is largely for use with the book; however, version 1.1 has a much greater focus on use with
    training materials, whilst retaining compatibility with the book.
	"""
	
	homepage = "https://www.ascent.io/"
	cran = "ascentTraining" 

	version("1.0.0", md5="e41407eb08f93dcc1d78e274112fa027")

	depends_on("r@3.5:", type=("build", "run"))
