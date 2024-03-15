# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDropletutils(RPackage):
	"""Utilities for Handling Single-Cell Droplet Data

	Provides a number of utility functions for handling single-cell (RNA-seq) data from droplet technologies such as 10X Genomics. This includes data loading from count matrices or molecule information files, identification of cells from empty droplets, removal of barcode-swapped pseudo-cells, and downsampling of the count matrix.
	"""
	
	bioc = "DropletUtils" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DropletUtils_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DropletUtils/DropletUtils_1.22.0.tar.gz"]

	version("1.22.0", md5="f1fe907e6269e652adc4607fdb335c41")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
