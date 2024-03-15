# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumi(RPackage):
	"""BeadArray Specific Methods for Illumina Methylation and Expression
	Microarrays.

	The lumi package provides an integrated solution for the Illumina
	microarray data analysis. It includes functions of Illumina BeadStudio
	(GenomeStudio) data input, quality control, BeadArray-specific variance
	stabilization, normalization and gene annotation at the probe level. It
	also includes the functions of processing Illumina methylation microarrays,
	especially Illumina Infinium methylation microarrays."""

	bioc = "lumi"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lumi_2.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lumi/lumi_2.54.0.tar.gz"]

	version("2.54.0", md5="59fdd5b0a2e145d7a8772635121bb2ec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-methylumi@2.3.2:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mgcv@1.4.0:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
