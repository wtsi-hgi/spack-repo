# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjmcmcnucleosomes(RPackage):
	"""Bayesian hierarchical model for genome-wide nucleosome positioning with high-throughput short-read data (MNase-Seq)

	This package does nucleosome positioning using informative Multinomial-Dirichlet prior in a t-mixture with reversible jump estimation of nucleosome positions for genome-wide profiling.
	"""
	
	homepage = "https://github.com/ArnaudDroitLab/RJMCMCNucleosomes"
	bioc = "RJMCMCNucleosomes"

	version("1.32.0", commit="6b4d501481c76a6e6b2f0935fb25054bdfcbf151")
	version("1.26.0", commit="a52bffdf089130e2f3f82ceb682f1ae60c8a14c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-consensusseeker", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
