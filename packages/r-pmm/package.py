# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmm(RPackage):
	"""Parallel Mixed Model

	The Parallel Mixed Model (PMM) approach is suitable for hit selection and cross-comparison of RNAi screens generated in experiments that are performed in parallel under several conditions. For example, we could think of the measurements or readouts from cells under RNAi knock-down, which are infected with several pathogens or which are grown from different cell lines.
	"""
	
	bioc = "pmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pmm_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pmm/pmm_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="3cbb5f74eeb15170c1d1cd4dfed4bf27e0ca2bbe5c860732edda917ffe009541")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
