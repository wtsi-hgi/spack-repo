# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIllumina450probevariantsDb(RPackage):
	"""Annotation Package combining variant data from 1000 Genomes Project for
	Illumina HumanMethylation450 Bead Chip probes.

	Includes details on variants for each probe on the 450k bead chip for each
	of the four populations (Asian, American, African and European)."""

	bioc = "Illumina450ProbeVariants.db"
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Illumina450ProbeVariants.db_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/Illumina450ProbeVariants.db/Illumina450ProbeVariants.db_1.38.0.tar.gz"]

	version("1.38.0", md5="ca34eec73a57e5f226b70a20ef706ee3")

	depends_on("r@3.0.1:", type=("build", "run"))

	# experiment