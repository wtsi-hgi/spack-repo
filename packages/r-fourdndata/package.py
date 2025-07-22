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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/fourDNData_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/fourDNData/fourDNData_1.2.0.tar.gz"]

	version("1.2.0", sha256="e0a778f11f46e0ac915a178a01e4eff37a9f34fdae56e1af49c39be24ea9bf19")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-hicexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

