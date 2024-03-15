# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlar(RPackage):
	"""Classification and Visualization.

	Miscellaneous functions for classification and visualization, e.g.
	regularized discriminant analysis, sknn() kernel-density naive Bayes, an
	interface to 'svmlight' and stepclass() wrapper variable selection for
	supervised classification, partimat() visualization of classification rules
	and shardsplot() of cluster results as well as kmodes() clustering for
	categorical data, corclust() variable clustering, variable extraction from
	different variable clustering models and weight of evidence
	preprocessing."""

	cran = "klaR"

	version("1.7-3", md5="8feef17d46c655d8bc7389c064c0afe6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-questionr", type=("build", "run"))

	# NOTE: The svmlight interface is not built. The external svmlight package
	# dates back to 2008, and does not build with modern compilers. In
	# addition, the tarfile is unversioned and its distribution is restricted.
