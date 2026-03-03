# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdsinrdata(RPackage):
	"""Data for the 'Mastering Health Data Science Using R' Online
Textbook

	Contains nine datasets used in the chapters and exercises of Paul, Alice (2023) "Health Data Science in R" <https://alicepaul.github.io/health-data-science-using-r/>.
	"""
	
	cran = "HDSinRdata" 

	version("0.1.1", md5="32adff9bb3ef2a92eb85ab7bc2bd437b")
	version("0.1.0", md5="47e7a4c693d7083faa71ee597d7e471a")

	depends_on("r@2.10:", type=("build", "run"))
