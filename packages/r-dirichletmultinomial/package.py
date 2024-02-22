# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirichletmultinomial(RPackage):
	"""Dirichlet-Multinomial Mixture Model Machine Learning for Microbiome
	Data.

	Dirichlet-multinomial mixture models can be used to describe variability
	in microbial metagenomic data. This package is an interface to code
	originally made available by Holmes, Harris, and Quince, 2012, PLoS ONE
	7(2): 1-15, as discussed further in the man page for this package,
	?DirichletMultinomial."""

	bioc = "DirichletMultinomial"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DirichletMultinomial_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DirichletMultinomial/DirichletMultinomial_1.44.0.tar.gz"]

	version("1.44.0", md5="8527c543b1ada9640d2f434fb516ff4e")

	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
