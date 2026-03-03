# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetscanHsEgDb(RPackage):
	"""TargetScan miRNA target predictions for human

	TargetScan miRNA target predictions for human assembled using data from the TargetScan website. TargetScan predicts biological targets of miRNAs by searching for the presence of conserved 8mer and 7mer sites that match the seed region of each miRNA. Also identified are sites with mismatches in the seed region that are compensated by conserved 3' pairing. In mammals, predictions are ranked based on the predicted efficacy of targeting as calculated using the context scores of the sites.
	"""
	
	bioc = "targetscan.Hs.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/targetscan.Hs.eg.db_0.6.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/targetscan.Hs.eg.db/targetscan.Hs.eg.db_0.6.1.tar.gz"]

	version("0.6.1", md5="d10569315400f6c1b95ad2688632b6de")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

