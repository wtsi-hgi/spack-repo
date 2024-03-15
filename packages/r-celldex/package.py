# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelldex(RPackage):
	"""Reference Index for Cell Types

	Provides a collection of reference expression datasets with curated cell type labels, for use in procedures like automated annotation of single-cell data or deconvolution of bulk RNA-seq.
	"""
	
	homepage = "https://github.com/LTLA/celldex"
	bioc = "celldex" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/celldex_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/celldex/celldex_1.12.0.tar.gz"]

	version("1.12.0", md5="62419c915beb91f7c228e1a125df68f8")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))

	# experiment