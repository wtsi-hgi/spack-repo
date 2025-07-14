# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcrank(RPackage):
	"""Predicting binding site consensus from ranked DNA sequences

	Functions and classes for de novo prediction of transcription factor binding consensus by heuristic search
	"""
	
	bioc = "BCRANK" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BCRANK_1.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BCRANK/BCRANK_1.64.0.tar.gz"]

	version("1.70.0", tag="RELEASE_3_21")
	version("1.64.0", sha256="496795e97de56be075d8dba2d51a19c7a83b834df68c06ee971c399f99622cd4")

	depends_on("r-biostrings", type=("build", "run"))
