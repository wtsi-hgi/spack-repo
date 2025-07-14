# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFccac(RPackage):
	"""functional Canonical Correlation Analysis to evaluate Covariance between nucleic acid sequencing datasets

	Computational evaluation of variability across DNA or RNA sequencing datasets is a crucial step in genomics, as it allows both to evaluate reproducibility of replicates, and to compare different datasets to identify potential correlations. fCCAC applies functional Canonical Correlation Analysis to allow the assessment of: (i) reproducibility of biological or technical replicates, analyzing their shared covariance in higher order components; and (ii) the associations between different datasets. fCCAC represents a more sophisticated approach that complements Pearson correlation of genomic coverage.
	"""
	
	bioc = "fCCAC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fCCAC_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fCCAC/fCCAC_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="1300c605487483ff3a13f7c1b2daedc087d1d3227644d1806335a26a8561e777")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-genomation", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
