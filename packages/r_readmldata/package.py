# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmldata(RPackage):
	"""Reading Machine Learning Benchmark Data Sets in Different
Formats

	Functions for reading data sets in different formats
  for testing machine learning tools are provided. This allows to run
  a loop over several data sets in their original form, for example
  if they are downloaded from UCI Machine Learning Repository.
  The data are not part of the package and have to be downloaded
  separately.
	"""
	
	homepage = "http://www.cs.cas.cz/~savicky/readMLData"
	cran = "readMLData" 

	version("0.9-7", md5="fdcd51c16ab5e6032590579bb5bd92a0")

	depends_on("r-xml", type=("build", "run"))
