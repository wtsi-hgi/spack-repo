# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatDb0(RPackage):
	"""Base Level Annotation databases for rat

	Base annotation databases for rat, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "rat.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rat.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rat.db0/rat.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="4c81e68b55f371206c8fbfc1f0f02f49d89e4a53a45d862b3c2e2cce017e02bc", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rat.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

