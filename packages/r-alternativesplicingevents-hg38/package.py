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

	version("1.1.0", commit="e05a08224c4db7806d219f32c05a4caa54a86227")
	version("1.1.0", commit="e05a08224c4db7806d219f32c05a4caa54a86227")

	depends_on("r-annotationhub", type=("build", "run"))

