# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdbUcscTrnas(RPackage):
	"""Annotation package for FeatureDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as FeatureDb objects
	"""
	
	bioc = "FDb.UCSC.tRNAs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.UCSC.tRNAs_1.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/FDb.UCSC.tRNAs/FDb.UCSC.tRNAs_1.0.1.tar.gz"]

	version("1.0.1", md5="77bfdadd4d9f995a72b001e4e41792fa")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation