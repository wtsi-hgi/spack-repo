# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlternativesplicingeventsHg38(RPackage):
	"""Alternative splicing event annotation for Human (hg38)

	Data frame containing alternative splicing events. The splicing events were compiled from the annotation files used by the alternative splicing quantification tools MISO, VAST-TOOLS, SUPPA and rMATS.
	"""
	
	homepage = "https://github.com/nuno-agostinho/alternativeSplicingEvents.hg38"
	bioc = "alternativeSplicingEvents.hg38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/alternativeSplicingEvents.hg38_1.1.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/alternativeSplicingEvents.hg38/alternativeSplicingEvents.hg38_1.1.0.tar.gz"]

	version("1.1.0", tag="RELEASE_3_21")
	version("1.1.0", sha256="ccad2bfc4e54227b8ca1231110534eb63b8a146bf99ac61d7aac26bddf5b0aa3", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/alternativeSplicingEvents.hg38_1.1.0.tar.gz")

	depends_on("r-annotationhub", type=("build", "run"))

