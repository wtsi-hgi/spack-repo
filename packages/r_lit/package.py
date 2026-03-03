# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLit(RPackage):
	"""Latent Interaction Testing for Genome-Wide Studies

	Identifying latent genetic interactions in genome-wide association studies
    using the Latent Interaction Testing (LIT) framework.
    LIT is a flexible kernel-based approach that leverages information across
    multiple traits to detect latent genetic interactions without specifying or
    observing the interacting variable (e.g., environment). LIT accepts
    standard PLINK files as inputs to analyze large genome-wide association studies.
	"""
	
	homepage = "https://github.com/ajbass/lit"
	cran = "lit" 

	version("1.0.0", md5="19c72922aee0ca28c1955b17b9a7fbb3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-genio", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
