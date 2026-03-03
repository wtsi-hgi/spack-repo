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

	version("1.1.0", md5="8d49710eebd62fb15a48cab252ff3eca", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/alternativeSplicingEvents.hg38_1.1.0.tar.gz")

	depends_on("r-annotationhub", type=("build", "run"))

