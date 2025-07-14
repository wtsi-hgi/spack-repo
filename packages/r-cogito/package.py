# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogito(RPackage):
	"""Compare genomic intervals tool - Automated, complete, reproducible and clear report about genomic and epigenomic data sets

	Biological studies often consist of multiple conditions which are examined with different laboratory set ups like RNA-sequencing or ChIP-sequencing. To get an overview about the whole resulting data set, Cogito provides an automated, complete, reproducible and clear report about all samples and basic comparisons between all different samples. This report can be used as documentation about the data set or as starting point for further custom analysis.
	"""
	
	bioc = "Cogito"

	version("1.14.0", commit="4c28c7ded88b2bb1800478afdf67ad0c3c235cae")
	version("1.8.0", commit="22931f7401e1fb5ef7d25f7ef83db7fe543e9227")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm9-knowngene", type=("build", "run"))
