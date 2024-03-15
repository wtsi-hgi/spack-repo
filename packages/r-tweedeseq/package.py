# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTweedeseq(RPackage):
	"""RNA-seq data analysis using the Poisson-Tweedie family of distributions

	Differential expression analysis of RNA-seq using the Poisson-Tweedie (PT) family of distributions. PT distributions are described by a mean, a dispersion and a shape parameter and include Poisson and NB distributions, among others, as particular cases. An important feature of this family is that, while the Negative Binomial (NB) distribution only allows a quadratic mean-variance relationship, the PT distributions generalizes this relationship to any orde.
	"""
	
	homepage = "https://github.com/isglobal-brge/tweeDEseq/"
	bioc = "tweeDEseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tweeDEseq_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tweeDEseq/tweeDEseq_1.48.0.tar.gz"]

	version("1.48.0", md5="1a919ba1b3c5709068bc126336b77826")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-cqn", type=("build", "run"))
