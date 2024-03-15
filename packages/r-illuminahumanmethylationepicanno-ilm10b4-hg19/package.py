# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylationepicannoIlm10b4Hg19(RPackage):
	"""Annotation for Illumina's EPIC methylation arrays."""

	bioc = "IlluminaHumanMethylationEPICanno.ilm10b4.hg19"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylationEPICanno.ilm10b4.hg19_0.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylationEPICanno.ilm10b4.hg19/IlluminaHumanMethylationEPICanno.ilm10b4.hg19_0.6.0.tar.gz"]

	version("0.6.0", md5="2d0c05917bcbf9ba1e354380d4e17a77", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylationEPICanno.ilm10b4.hg19_0.6.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-minfi@1.19.15:", type=("build", "run"))

	# annotation