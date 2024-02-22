# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimorhyde2(RPackage):
	"""Quantify Rhythmicity and Differential Rhythmicity in Genomic
Data

	Fit linear models based on periodic splines, moderate model
  coefficients using multivariate adaptive shrinkage, then compute properties of
  the moderated curves.
	"""
	
	homepage = "https://limorhyde2.hugheylab.org"
	cran = "limorhyde2" 

	version("0.1.0", md5="c6dd58c9edacda384d7c2fa26ca5a70e", url="https://cran.r-project.org/src/contrib/limorhyde2_0.1.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-ashr@2.2.54:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-deseq2@1.30:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-hdinterval@0.2.2:", type=("build", "run"))
	depends_on("r-iterators@1.0.12:", type=("build", "run"))
	depends_on("r-limma@3.42.2:", type=("build", "run"))
	depends_on("r-mashr@0.2.50:", type=("build", "run"))
	depends_on("r-pbs@1.1:", type=("build", "run"))
	depends_on("r-zeallot@0.1:", type=("build", "run"))
