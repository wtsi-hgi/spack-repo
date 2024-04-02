# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPing(RPackage):
	"""Probabilistic inference for Nucleosome Positioning with MNase-based or Sonicated Short-read Data

	Probabilistic inference of ChIP-Seq using an empirical Bayes mixture model approach.
	"""
	
	bioc = "PING" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PING_2.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PING/PING_2.46.0.tar.gz"]

	version("2.46.0", md5="703e11e3d890a3cf2b48c15d4c76ea87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pics", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
