# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbmix(RPackage):
	"""Bayesian Model for Genotyping using RNA-Seq

	The method models RNA-seq reads using a mixture of 3 beta-binomial distributions to generate posterior probabilities for genotyping bi-allelic single nucleotide polymorphisms. Elena Vigorito, Anne Barton, Costantino Pitzalis, Myles J. Lewis and Chris Wallace (2023) <doi:10.1093/bioinformatics/btad393> "BBmix: a Bayesian beta-binomial mixture model for accurate genotyping from RNA-sequencing."
	"""
	
	cran = "bbmix" 

	version("1.0.0", md5="361fc95fc67fe69aa2be7a076e5e4d55")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "link", "run"))
