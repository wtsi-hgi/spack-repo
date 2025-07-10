# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecountmethylation(RPackage):
	"""Access and analyze public DNA methylation array data compilations

	Resources for cross-study analyses of public DNAm array data from NCBI GEO repo, produced using Illumina's Infinium HumanMethylation450K (HM450K) and MethylationEPIC (EPIC) platforms. Provided functions enable download, summary, and filtering of large compilation files. Vignettes detail background about file formats, example analyses, and more. Note the disclaimer on package load and consult the main manuscripts for further info.
	"""
	
	homepage = "https://github.com/metamaden/recountmethylation"
	bioc = "recountmethylation" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/recountmethylation_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/recountmethylation/recountmethylation_1.12.0.tar.gz"]

	version("1.12.0", sha256="141d3a3dc74aa44398c214398c25b39fe74efb06e0844d370e9bef60531567ff")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
