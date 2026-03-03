# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAromaCn(RPackage):
	"""Copy-Number Analysis of Large Microarray Data Sets

	Methods for analyzing DNA copy-number data.  Specifically,
  this package implements the multi-source copy-number normalization (MSCN)
  method for normalizing copy-number data obtained on various platforms and
  technologies.  It also implements the TumorBoost method for normalizing
  paired tumor-normal SNP data.
	"""
	
	homepage = "https://www.aroma-project.org/"
	cran = "aroma.cn" 

	version("1.7.1", md5="9f6b2f102cbfd11e60b00ce20dc6cd03")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-r-utils@2.11:", type=("build", "run"))
	depends_on("r-aroma-core@3.2.2:", type=("build", "run"))
	depends_on("r-r-methodss3@1.8.1:", type=("build", "run"))
	depends_on("r-r-oo@1.24:", type=("build", "run"))
	depends_on("r-r-filesets@2.14:", type=("build", "run"))
	depends_on("r-r-cache@0.15:", type=("build", "run"))
	depends_on("r-matrixstats@0.61:", type=("build", "run"))
	depends_on("r-pscbs@0.65:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
