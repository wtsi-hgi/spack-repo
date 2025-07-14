# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindit2(RPackage):
	"""find influential TF and Target based on multi-omics data

	This package implements functions to find influential TF and target based on different input type. It have five module: Multi-peak multi-gene annotaion(mmPeakAnno module), Calculate regulation potential(calcRP module), Find influential Target based on ChIP-Seq and RNA-Seq data(Find influential Target module), Find influential TF based on different input(Find influential TF module), Calculate peak-gene or peak-peak correlation(peakGeneCor module). And there are also some other useful function like integrate different source information, calculate jaccard similarity for your TF.
	"""
	
	homepage = "https://github.com/shangguandong1996/FindIT2"
	bioc = "FindIT2"

	version("1.14.0", commit="b0f7ffcef96a11522424541139afd89d96c9396c")
	version("1.8.0", commit="f4ef6c4bca5d7b5427a5755ae2c461598192c343")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
