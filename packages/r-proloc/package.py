# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProloc(RPackage):
	"""A unifying bioinformatics framework for spatial proteomics

	The pRoloc package implements machine learning and visualisation methods for the analysis and interogation of quantitiative mass spectrometry data to reliably infer protein sub-cellular localisation.
	"""
	
	homepage = "https://github.com/lgatto/pRoloc"
	bioc = "pRoloc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pRoloc_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pRoloc/pRoloc_1.42.0.tar.gz"]

	version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="fa0a6e4c7cc0247d5fd67458db8fc9e2e3a05cad4da9b785b10c4c911e9bad93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msnbase@1.19.20:", type=("build", "run"))
	depends_on("r-mlinterfaces@1.67.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mclust@4.3:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
