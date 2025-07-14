# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabomxtr(RPackage):
	"""A package to run mixture models for truncated metabolomics data with normal or lognormal distributions

	The functions in this package return optimized parameter estimates and log likelihoods for mixture models of truncated data with normal or lognormal distributions.
	"""
	
	bioc = "metabomxtr"

	version("1.42.0", commit="261703f6eaa72a5c846e568c2863e0a25e5bd992")
	version("1.36.0", commit="1e127d0137ba394dab424d8b603dfd9b16d9a3e8")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
