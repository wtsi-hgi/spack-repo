# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLymphoseqdb(RPackage):
	"""LymphoSeq annotation databases

	This package provides annotation databases that support the package LymphoSeq.
	"""
	
	bioc = "LymphoSeqDB" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/LymphoSeqDB_0.99.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/LymphoSeqDB/LymphoSeqDB_0.99.2.tar.gz"]

	version("0.99.2", md5="22fc0dc2439ef497982a5ffddda1e418")

	depends_on("r@3.2:", type=("build", "run"))

	# annotation