# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComet(RPackage):
	"""coMET: visualisation of regional epigenome-wide association scan (EWAS) results and DNA co-methylation patterns

	Visualisation of EWAS results in a genomic region. In addition to phenotype-association P-values, coMET also generates plots of co-methylation patterns and provides a series of annotation tracks. It can be used to other omic-wide association scans as lon:g as the data can be translated to genomic level and for any species.
	"""
	
	homepage = "http://epigen.kcl.ac.uk/comet"
	bioc = "coMET" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/coMET_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/coMET/coMET_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="bfb9106e278fce62abde5a823e3fea42fc9515f174af8511f249aebc99b370de")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
