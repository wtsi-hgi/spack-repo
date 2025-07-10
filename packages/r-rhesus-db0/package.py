# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhesusDb0(RPackage):
	"""Base Level Annotation databases for rhesus

	Base annotation databases for rhesus, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "rhesus.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rhesus.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rhesus.db0/rhesus.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="e16f47c1bcb824d0af0085e32bb0f3445743a063fa82e4e9f96330e577d68022", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rhesus.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

