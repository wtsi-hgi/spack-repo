# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFission(RPackage):
	"""RangedSummarizedExperiment for time course RNA-Seq of fission yeast in response to stress, by Leong et al., Nat Commun 2014.

	This package provides a RangedSummarizedExperiment object of read counts in genes for a time course RNA-Seq experiment of fission yeast (Schizosaccharomyces pombe) in response to oxidative stress (1M sorbitol treatment) at 0, 15, 30, 60, 120 and 180 mins. The samples are further divided between a wild-type group and a group with deletion of atf21. The read count matrix was prepared and provided by the author of the study: Leong HS, Dawson K, Wirth C, Li Y, Connolly Y, Smith DL, Wilkinson CR, Miller CJ. "A global non-coding RNA system modulates fission yeast protein levels in response to stress". Nat Commun 2014 May 23;5:3947. PMID: 24853205. GEO: GSE56761.
	"""
	
	bioc = "fission"

	version("1.28.0", commit="d5736634a3d82331e41a119c386bf2cd2840fa0c")
	version("1.22.0", commit="efef834642411af49357d5a42eff6986a3446dbf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

