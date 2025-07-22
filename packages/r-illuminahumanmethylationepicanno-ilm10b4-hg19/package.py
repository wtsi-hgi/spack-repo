# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylationepicannoIlm10b4Hg19(RPackage):
	"""Annotation for Illumina's EPIC methylation arrays."""

	bioc = "IlluminaHumanMethylationEPICanno.ilm10b4.hg19"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylationEPICanno.ilm10b4.hg19_0.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylationEPICanno.ilm10b4.hg19/IlluminaHumanMethylationEPICanno.ilm10b4.hg19_0.6.0.tar.gz"]
	
	version("0.6.0", sha256="2c8128126b63e7fa805a5f3b02449367dca9c3be3eb5f6300acc718826590719", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylationEPICanno.ilm10b4.hg19_0.6.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-minfi@1.19.15:", type=("build", "run"))

