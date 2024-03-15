# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse13015(RPackage):
	"""GEO accession data GSE13015_GPL6106 as a SummarizedExperiment

	Microarray expression matrix platform GPL6106 and clinical data for 67 septicemic patients and made them available as GEO accession [GSE13015](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE13015). GSE13015 data have been parsed into a SummarizedExperiment object available in ExperimentHub. This data data could be used as an example supporting BloodGen3Module R package.
	"""
	
	bioc = "GSE13015" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GSE13015_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GSE13015/GSE13015_1.10.0.tar.gz"]

	version("1.10.0", md5="99fae6872abf6820842a1340f7fd6b4e", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GSE13015_1.10.0.tar.gz")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment