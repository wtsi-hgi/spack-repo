# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabstats(RPackage):
	"""Data Sets for the Book "Experimental Design for Laboratory
Biologists"

	Contains data sets to accompany the book: Lazic SE
    (2016). "Experimental Design for Laboratory Biologists: Maximising Information
    and Improving Reproducibility". Cambridge University Press.
	"""
	
	homepage = "https://github.com/stanlazic/labstats"
	cran = "labstats" 

	version("1.0.1", md5="6617bed93ae3de7afc728f0ff09778a9")

	depends_on("r@2.10:", type=("build", "run"))
