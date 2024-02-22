# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdaseq(RPackage):
	"""Exploratory Data Analysis and Normalization for RNA-Seq

	Numerical and graphical summaries of RNA-Seq read data. Within-lane normalization procedures to adjust for GC-content effect (or other gene-level effects) on read counts: loess robust local regression, global-scaling, and full-quantile normalization (Risso et al., 2011). Between-lane normalization procedures to adjust for distributional differences between lanes (e.g., sequencing depth): global-scaling and full-quantile normalization (Bullard et al., 2010).
	"""
	
	homepage = "https://github.com/drisso/EDASeq"
	bioc = "EDASeq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EDASeq_2.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EDASeq/EDASeq_2.36.0.tar.gz"]

	version("2.36.0", md5="b2d28fdad31e8c56f68873b599ffc235")

	depends_on("r-biobase@2.15.1:", type=("build", "run"))
	depends_on("r-shortread@1.11.42:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges@1.13.9:", type=("build", "run"))
	depends_on("r-aroma-light", type=("build", "run"))
	depends_on("r-rsamtools@1.5.75:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
