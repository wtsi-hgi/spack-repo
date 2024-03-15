# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenxio(RPackage):
	"""Import methods for 10X Genomics files

	Provides a structured S4 approach to importing data files from the 10X pipelines. It mainly supports Single Cell Multiome ATAC + Gene Expression data among other data types. The main Bioconductor data representations used are SingleCellExperiment and RaggedExperiment.
	"""
	
	homepage = "https://github.com/waldronlab/TENxIO"
	bioc = "TENxIO" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TENxIO_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TENxIO/TENxIO_1.4.0.tar.gz"]

	version("1.4.0", md5="98a845f55877d89b82b9a153fe54a41f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
