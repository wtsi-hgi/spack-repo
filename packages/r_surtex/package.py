# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurtex(RPackage):
	"""LaTeX descriptive statistic reporting for survey data

	suRtex was designed for easy descriptive statistic reporting of categorical survey data (e.g., Likert scales) in LaTeX. suRtex takes a matrix or data frame and produces the LaTeX code necessary for a sideways table creation. Mean, median, standard deviation, and sample size are optional.
	"""
	
	cran = "suRtex" 

	version("0.9", md5="fc877a6ae441fed36a84e69e79abca46")

