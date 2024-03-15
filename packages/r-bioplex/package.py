# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioplex(RPackage):
	"""R-side access to BioPlex protein-protein interaction data

	The BioPlex package implements access to the BioPlex protein-protein interaction networks and related resources from within R. Besides protein-protein interaction networks for HEK293 and HCT116 cells, this includes access to CORUM protein complex data, and transcriptome and proteome data for the two cell lines. Functionality focuses on importing the various data resources and storing them in dedicated Bioconductor data structures, as a foundation for integrative downstream analysis of the data.
	"""
	
	homepage = "https://github.com/ccb-hms/BioPlex"
	bioc = "BioPlex" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/BioPlex_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/BioPlex/BioPlex_1.8.0.tar.gz"]

	version("1.8.0", md5="77e38da3b194e7776fa7007a2cef42bf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))

	# experiment