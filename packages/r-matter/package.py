# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatter(RPackage):
	"""Out-of-memory dense and sparse signal arrays

	Memory-efficient file-based data structures for dense and sparse vectors, matrices, arrays, and lists with applications to nonuniformly sampled signals and spectra.
	"""
	
	homepage = "https://github.com/kuwisdelu/matter"
	bioc = "matter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/matter_2.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/matter/matter_2.4.0.tar.gz"]

	version("2.4.0", md5="08919bc0df5442e0916ee7cffbc23003")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-biglm", type=("build", "run"))
