# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdductomicsr(RPackage):
	"""Processing of adductomic mass spectral datasets

	Processes MS2 data to identify potentially adducted peptides from spectra that has been corrected for mass drift and retention time drift and quantifies MS1 level mass spectral peaks.
	"""
	
	bioc = "adductomicsR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/adductomicsR_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/adductomicsR/adductomicsR_1.18.0.tar.gz"]

	version("1.18.0", md5="82e24a09ba891b76e9497a6725b96fe0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-adductdata", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-orgmassspecr@0.4.6:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-mzr@2.14:", type=("build", "run"))
	depends_on("r-ade4@1.7.6:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-pastecs@1.3.18:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-pracma@2.0.4:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-fpc@2.1.10:", type=("build", "run"))
	depends_on("r-dosnow@1.0.14:", type=("build", "run"))
	depends_on("r-fastcluster@1.1.22:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-bootstrap@2017.2:", type=("build", "run"))
	depends_on("r-smoother@1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-zoo@1.8:", type=("build", "run"))
