# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipseqdbdata(RPackage):
	"""Data for the chipseqDB Workflow

	Sorted and indexed BAM files for ChIP-seq libraries, for use in the chipseqDB workflow. BAM indices are also included.
	"""
	
	bioc = "chipseqDBData"

	version("1.24.0", commit="67266988cdf0e1d5a5a1f2e613c053b80a09ee36")
	version("1.18.0", commit="97dccfe92359c6254faac81e5cfd2d3ea6ec14e7")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

