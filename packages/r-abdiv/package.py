# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbdiv(RPackage):
	"""Alpha and Beta Diversity Measures

	A collection of measures for measuring ecological diversity.
  Ecological diversity comes in two flavors: alpha diversity measures the
  diversity within a single site or sample, and beta diversity measures the
  diversity across two sites or samples. This package overlaps considerably
  with other R packages such as 'vegan', 'gUniFrac', 'betapart', and 'fossil'.
  We also include a wide range of functions that are implemented in software
  outside the R ecosystem, such as 'scipy', 'Mothur', and 'scikit-bio'.  The
  implementations here are designed to be basic and clear to the reader.
	"""
	
	homepage = "https://github.com/kylebittinger/abdiv"
	cran = "abdiv" 

	version("0.2.0", md5="80931c0ca85ba5386000bf617552c5ce")

	depends_on("r-ape", type=("build", "run"))
