# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlternativesplicingeventsHg19(RPackage):
	"""Alternative splicing event annotation for Human (hg19)

	Data frame containing alternative splicing events. The splicing events were compiled from the annotation files used by the alternative splicing quantification tools MISO, VAST-TOOLS, SUPPA and rMATS.
	"""
	
	homepage = "https://github.com/nuno-agostinho/alternativeSplicingEvents.hg19"
	bioc = "alternativeSplicingEvents.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/alternativeSplicingEvents.hg19_1.1.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/alternativeSplicingEvents.hg19/alternativeSplicingEvents.hg19_1.1.0.tar.gz"]

	version("1.1.0", sha256="1ed48574b920ec11bf69decba1c387a1d58803a6294036ac5fdf18dd06b72061", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/alternativeSplicingEvents.hg19_1.1.0.tar.gz")

	depends_on("r-annotationhub", type=("build", "run"))

