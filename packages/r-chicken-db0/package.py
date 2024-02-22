# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChickenDb0(RPackage):
	"""Base Level Annotation databases for chicken

	Base annotation databases for chicken, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "chicken.db0" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/chicken.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/chicken.db0/chicken.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="0f0c20a519a9490c0909b68ec67c206d", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/chicken.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation