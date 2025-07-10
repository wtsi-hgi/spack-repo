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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chicken.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/chicken.db0/chicken.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="824e7ee3e9d7aea9d88e815399d33236b170939a2cb1a75a79cdd4dae5ba5eac", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chicken.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

