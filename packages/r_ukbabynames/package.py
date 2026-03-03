# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkbabynames(RPackage):
	"""UK Baby Names Data

	Full listing of UK baby names occurring more than three times per year between 1974 and 2020, and rankings of baby name popularity by decade from 1904 to 1994.
	"""
	
	homepage = "https://mine-cetinkaya-rundel.github.io/ukbabynames/"
	cran = "ukbabynames" 

	version("0.3.0", md5="ae8ed8e725ca76f13a48d3c736c68bb2")

	depends_on("r@2.10:", type=("build", "run"))
