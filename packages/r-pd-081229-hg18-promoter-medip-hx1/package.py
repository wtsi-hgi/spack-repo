# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPd081229Hg18PromoterMedipHx1(RPackage):
	"""Platform Design Info for NimbleGen 081229_hg18_promoter_medip_hx1

	Platform Design Info for NimbleGen 081229_hg18_promoter_medip_hx1
	"""
	
	bioc = "pd.081229.hg18.promoter.medip.hx1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.081229.hg18.promoter.medip.hx1_0.99.4.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.081229.hg18.promoter.medip.hx1/pd.081229.hg18.promoter.medip.hx1_0.99.4.tar.gz"]

	version("0.99.4", md5="f3c240fa0d4503e94047be5ee323856b", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.081229.hg18.promoter.medip.hx1_0.99.4.tar.gz")
	version("0.99.4", md5="f3c240fa0d4503e94047be5ee323856b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.081229.hg18.promoter.medip.hx1_0.99.4.tar.gz")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rsqlite@0.7.1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.9.30:", type=("build", "run"))
	depends_on("r-oligo@1.11.18:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.13.50:", type=("build", "run"))
	depends_on("r-iranges@1.3.89:", type=("build", "run"))

