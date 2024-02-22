# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistdat(RPackage):
	"""Summary Statistics for Histogram/Count Data

	In some cases you will have data in a histogram format, where
  you have a vector of all possible observations, and a vector of how many
  times each observation appeared. You could expand this into a single 1D
  vector, but this may not be advisable if the counts are extremely large.
  'HistDat' allows for the calculation of summary statistics without the need
  for expanding your data.
	"""
	
	cran = "HistDat" 

	version("0.2.0", md5="b3e0138b1eaf4dd2ad029e33c319a7fa")

