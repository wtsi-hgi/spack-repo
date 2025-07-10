# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacrophage(RPackage):
	"""Human macrophage immune response

	This package provides the output of running Salmon on a set of 24 RNA-seq samples from Alasoo, et al. "Shared genetic effects on chromatin and gene expression indicate a role for enhancer priming in immune response", published in Nature Genetics, January 2018. For details on version numbers and how the samples were processed see the package vignette.
	"""
	
	bioc = "macrophage" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/macrophage_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/macrophage/macrophage_1.18.0.tar.gz"]

	version("1.18.0", sha256="be731cf53cf595dab3ba56562606a874cd82890405220e2df1ae4347c64ea681")

	depends_on("r@3.5:", type=("build", "run"))

