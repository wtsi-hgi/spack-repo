# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpannot(RPackage):
	"""Anotation package for Hipathia package

	Package containing example and annotation data for Hipathia package. Hipathia is a method for the computation of signal transduction along signaling pathways from transcriptomic data. The method is based on an iterative algorithm which is able to compute the signal intensity passing through the nodes of a network by taking into account the level of expression of each gene and the intensity of the signal arriving to it. It also provides a new approach to functional analysis allowing to compute the signal arriving to the functions annotated to each pathway. Hipathia depends on this package to be functional.
	"""
	
	bioc = "hpAnnot" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hpAnnot_1.1.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hpAnnot/hpAnnot_1.1.0.tar.gz"]

	version("1.1.0", md5="fbc94a00b0f33b41bc5ff53fbe060663")

	depends_on("r@3.5:", type=("build", "run"))

