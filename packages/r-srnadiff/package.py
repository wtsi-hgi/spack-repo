# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrnadiff(RPackage):
	"""Finding differentially expressed unannotated genomic regions from RNA-seq data

	srnadiff is a package that finds differently expressed regions from RNA-seq data at base-resolution level without relying on existing annotation. To do so, the package implements the identify-then-annotate methodology that builds on the idea of combining two pipelines approachs differential expressed regions detection and differential expression quantification. It reads BAM files as input, and outputs a list differentially regions, together with the adjusted p-values.
	"""
	
	bioc = "srnadiff" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/srnadiff_1.22.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/srnadiff/srnadiff_1.22.2.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.2", sha256="15fd032d853044ce1879f83152750e014a6aa1b47fd969e61869288665960d1a")
	version("1.22.0", md5="0125777227eab34f7839615139aacb91")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
