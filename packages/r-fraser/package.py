# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFraser(RPackage):
	"""Find RAre Splicing Events in RNA-Seq Data

	Detection of rare aberrant splicing events in transcriptome profiles. Read count ratio expectations are modeled by an autoencoder to control for confounding factors in the data. Given these expectations, the ratios are assumed to follow a beta-binomial distribution with a junction specific dispersion. Outlier events are then identified as read-count ratios that deviate significantly from this distribution. FRASER is able to detect alternative splicing, but also intron retention. The package aims to support diagnostics in the field of rare diseases where RNA-seq is performed to identify aberrant splicing defects.
	"""
	
	homepage = "https://github.com/gagneurlab/FRASER"
	bioc = "FRASER" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FRASER_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FRASER/FRASER_1.14.1.tar.gz"]

    version("2.4.3", tag="RELEASE_3_21")
	version("1.14.1", sha256="3cc9a84cbe1ddfcc0a7c09df54e01b364a435940d825814bf564b90135bf438f")

	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-delayedarray@0.5.11:", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-outrider", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rsubread", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
