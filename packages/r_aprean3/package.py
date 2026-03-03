# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAprean3(RPackage):
	"""Datasets from Draper and Smith "Applied Regression Analysis"
(3rd Ed., 1998)

	An unofficial companion to the textbook "Applied Regression
    Analysis" by N.R. Draper and H. Smith (3rd Ed., 1998) including all the
    accompanying datasets.
	"""
	
	homepage = "https://github.com/lbraglia/aprean3"
	cran = "aprean3" 

	version("1.0.1", md5="26d50529f38b6a7218877e16cc149d56", url="https://cran.r-project.org/src/contrib/aprean3_1.0.1.tar.gz")

	depends_on("r@3.1.1:", type=("build", "run"))
