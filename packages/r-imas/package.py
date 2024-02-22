# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImas(RPackage):
	"""Integrative analysis of Multi-omics data for Alternative Splicing

	Integrative analysis of Multi-omics data for Alternative splicing.
	"""
	
	bioc = "IMAS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IMAS_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IMAS/IMAS_1.26.0.tar.gz"]

	version("1.26.0", md5="c86deaedf1d19981dbfcea7a3b53d331")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ivas", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
