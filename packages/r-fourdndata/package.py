# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFourdndata(RPackage):
	"""4DN data package

	fourDNData is a data package giving programmatic access to Hi-C contact matrices uniformly processed by the [4DN consortium](https://www.4dnucleome.org/). The matrices are available in the multi-resolution `.mcool` format.
	"""
	
	homepage = "https://github.com/js2264/fourDNData"
	bioc = "fourDNData"

	version("1.8.0", commit="79cb8b4ca5ea55b0f24b216496c6549e4f9f69d7")
	version("1.2.0", commit="89ed36401615142ff8be7fdbf887e27dd914499f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-hicexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

